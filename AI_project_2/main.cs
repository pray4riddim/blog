using System;
using System.Collections.Generic;

namespace EightPuzzle
{
    class Node : IComparable<Node>
    {
        public string state;
        public int f, g, h;
        public int zeroPos;

        public Node(string s)
        {
            state = s;
            g = 0;
            h = getHeuristic();
            f = g + h;
            zeroPos = state.IndexOf('0');
        }

        public int CompareTo(Node other)
        {
            return f - other.f;
        }

        public int getHeuristic()
        {
            int heuristic = 0;
            for (int i = 0; i < state.Length; i++)
            {
                if (state[i] != '0')
                {
                    int num = int.Parse(state[i].ToString());
                    int row = num / 3;
                    int col = num % 3;
                    int goalRow = row;
                    int goalCol = col;
                    for (int j = 0; j < state.Length; j++)
                    {
                        if (state[j] == char.Parse(num.ToString()))
                        {
                            goalRow = j / 3;
                            goalCol = j % 3;
                            break;
                        }
                    }
                    heuristic += Math.Abs(row - goalRow) + Math.Abs(col - goalCol);
                }
            }
            return heuristic;
        }

        public List<Node> getSuccessors()
        {
            List<Node> successors = new List<Node>();
            int row = zeroPos / 3;
            int col = zeroPos % 3;
            if (row > 0) // move up
            {
                string newState = swap(state, zeroPos, zeroPos - 3);
                successors.Add(new Node(newState));
            }
            if (row < 2) // move down
            {
                string newState = swap(state, zeroPos, zeroPos + 3);
                successors.Add(new Node(newState));
            }
            if (col > 0) // move left
            {
                string newState = swap(state, zeroPos, zeroPos - 1);
                successors.Add(new Node(newState));
            }
            if (col < 2) // move right
            {
                string newState = swap(state, zeroPos, zeroPos + 1);
                successors.Add(new Node(newState));
            }
            return successors;
        }

        private string swap(string s, int i, int j)
        {
            char[] chars = s.ToCharArray();
            char temp = chars[i];
            chars[i] = chars[j];
            chars[j] = temp;
            return new string(chars);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            string initialState = args[0];
            string goalState = args[1];

            Node startNode = new Node(initialState);
            Node goalNode = new Node(goalState);

            HashSet<string> closedSet = new HashSet<string>();
            PriorityQueue<Node> openSet = new PriorityQueue<Node>();

            openSet.Enqueue(startNode);

            while (openSet.Count > 0)
            {
                Node current = openSet.Dequeue();
                if (current.state == goalState)
                {
                    printSolution(current);
                    return;
                }
                closedSet.Add(current.state);
                foreach (Node successor in current.getSuccessors())
                {
                    if (closedSet.Contains(successor.state))
                    {
                        continue;
                    }
                    int tentativeG = current.g + 1;
                    if (!openSet.Contains(successor) || tentativeG < successor.g)
                    {
                        successor.g = tentativeG;
                        successor.f = successor.g + successor.h;
                        openSet.Enqueue(successor);
                    }
                }
            }

            Console.WriteLine("No solution found.");
        }

        static void printSolution(Node node)
        {
            if (node == null)
            {
                return;
            }
            printSolution(node.parent);
            Console.WriteLine(node.state);
        }
    }

    class PriorityQueue<T> where T : IComparable<T>
    {
        private List<T> data;

        public PriorityQueue()
        {
            this.data = new List<T>();
        }

        public void Enqueue(T item)
        {
            data.Add(item);
            int ci = data.Count - 1; // child index; start at end
            while (ci > 0)
            {
                int pi = (ci - 1) / 2; // parent index
                if (data[ci].CompareTo(data[pi]) >= 0)
                {
                    break; // child item is larger than (or equal) parent so we're done
                }
                T tmp = data[ci];
                data[ci] = data[pi];
                data[pi] = tmp;
                ci = pi;
            }
        }

        public T Dequeue()
        {
            // assumes pq is not empty; up to calling code
            int li = data.Count - 1; // last index (before removal)
            T frontItem = data[0];   // fetch the front
            data[0] = data[li];
            data.RemoveAt(li);

            --li; // last index (after removal)
            int pi = 0; // parent index. start at front of pq
            while (true)
            {
                int ci = pi * 2 + 1; // left child index of parent
                if (ci > li)
                {
                    break;  // no children so done
                }
                int rc = ci + 1;     // right child
                if (rc <= li && data[rc].CompareTo(data[ci]) < 0)
                {
                    ci = rc; // prefer smallest child
                }
                if (data[pi].CompareTo(data[ci]) <= 0)
                {
                    break; // parent is smaller than (or equal to) smallest child so done
                }
                T tmp = data[pi];
                data[pi] = data[ci];
                data[ci] = tmp; // swap parent and child
                pi = ci;
            }
            return frontItem;
        }

        public int Count
        {
            get { return data.Count; }
        }

        public override string ToString()
        {
            string s = "";
            for (int i = 0; i < data.Count; ++i)
                s += data[i].ToString() + " ";
            s += "count = " + data.Count;
            return s;
        }

        public bool Contains(T item)
        {
            return data.Contains(item);
        }
    }
}
