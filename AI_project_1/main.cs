using System;
using System.Collections.Generic;

namespace MissionariesAndCannibals
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Please input n: ");
            int n = int.Parse(Console.ReadLine());

            Console.Write("Please input c: ");
            int c = int.Parse(Console.ReadLine());

            List<string> optimalProcedure = SolveMissionariesAndCannibals(n, c);
            if (optimalProcedure.Count == 0)
            {
                Console.WriteLine("Failed");
            }
            else
            {
                Console.WriteLine("Successed");
                Console.Write("Optimal Procedure: ");
                foreach (string step in optimalProcedure)
                {
                    Console.Write(step + "->");
                }
                Console.WriteLine("000");
            }
        }

        static List<string> SolveMissionariesAndCannibals(int n, int c)
        {
            List<string> optimalProcedure = new List<string>();
            State initialState = new State(n, n, 1);
            State targetState = new State(0, 0, 0);

            Queue<State> stateQueue = new Queue<State>();
            stateQueue.Enqueue(initialState);

            Dictionary<State, State> parentStates = new Dictionary<State, State>();
            parentStates.Add(initialState, null);

            while (stateQueue.Count > 0)
            {
                State currentState = stateQueue.Dequeue();

                if (currentState.Equals(targetState))
                {
                    while (currentState != null)
                    {
                        optimalProcedure.Insert(0, currentState.ToString());
                        currentState = parentStates[currentState];
                    }
                    break;
                }

                List<State> nextStates = GetNextStates(currentState, n, c);
                foreach (State nextState in nextStates)
                {
                    if (!parentStates.ContainsKey(nextState))
                    {
                        stateQueue.Enqueue(nextState);
                        parentStates.Add(nextState, currentState);
                    }
                }
            }

            return optimalProcedure;
        }

        static List<State> GetNextStates(State currentState, int n, int c)
        {
            List<State> nextStates = new List<State>();

            int boatPosition = currentState.BoatPosition;

            for (int m = 0; m <= c; m++)
            {
                for (int w = 0; w <= c - m; w++)
                {
                    if (m + w > 0 && m + w <= c && (currentState.MissionariesOnStartBank >= m || currentState.MissionariesOnBoat >= m) &&
                        (currentState.CannibalsOnStartBank >= w || currentState.CannibalsOnBoat >= w))
                    {
                        int missionariesOnStartBank = currentState.MissionariesOnStartBank - m;
                        int cannibalsOnStartBank = currentState.CannibalsOnStartBank - w;

                        int missionariesOnBoat = currentState.MissionariesOnBoat + m;
                        int cannibalsOnBoat = currentState.CannibalsOnBoat + w;

                        int missionariesOnTargetBank = n - missionariesOnStartBank - missionariesOnBoat;
                        int cannibalsOnTargetBank = n - cannibalsOnStartBank - cannibalsOnBoat;

                        if ((missionariesOnStartBank == 0 || missionariesOnStartBank >= cannibalsOnStartBank) &&
                            (missionariesOnTargetBank == 0 || missionariesOnTargetBank >= cannibalsOnTargetBank))
                        {
                            State nextState = new State(missionariesOnStartBank, cannibalsOnStartBank, boatPosition == 1 ? 0 : 1,
                                missionariesOnBoat, cannibalsOnBoat);
                            nextStates.Add(nextState);
                        }
                    }
                }
            }

            return nextStates;
        }
    }

    class State
    {
        public int MissionariesOnStartBank { get; }
        public int CannibalsOnStartBank { get; }
        public int BoatPosition { get; }
        public int MissionariesOnBoat { get; }
        public int CannibalsOnBoat { get; }

        public State(int missionariesOnStartBank, int cannibalsOnStartBank, int boatPosition,
            int missionariesOnBoat = 0, int cannibalsOnBoat = 0)
        {
            MissionariesOnStartBank = missionariesOnStartBank;
            CannibalsOnStartBank = cannibalsOnStartBank;
            BoatPosition = boatPosition;
            MissionariesOnBoat = missionariesOnBoat;
            CannibalsOnBoat = cannibalsOnBoat;
        }

        public override bool Equals(object obj)
        {
            if (obj == null || GetType() != obj.GetType())
                return false;

            State otherState = (State)obj;
            return MissionariesOnStartBank == otherState.MissionariesOnStartBank &&
                   CannibalsOnStartBank == otherState.CannibalsOnStartBank &&
                   BoatPosition == otherState.BoatPosition &&
                   MissionariesOnBoat == otherState.MissionariesOnBoat &&
                   CannibalsOnBoat == otherState.CannibalsOnBoat;
        }

        public override int GetHashCode()
        {
            int hash = 17;
            hash = hash * 23 + MissionariesOnStartBank.GetHashCode();
            hash = hash * 23 + CannibalsOnStartBank.GetHashCode();
            hash = hash * 23 + BoatPosition.GetHashCode();
            hash = hash * 23 + MissionariesOnBoat.GetHashCode();
            hash = hash * 23 + CannibalsOnBoat.GetHashCode();
            return hash;
        }


        public override string ToString()
        {
            return $"{MissionariesOnStartBank}{CannibalsOnStartBank}{BoatPosition}";
        }
    }
}
