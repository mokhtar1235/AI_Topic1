# AI_Topic1_5245064
Problem Solving Methods
Introduction:
“All life is problem solving.”
—Karl Popper [1]
Problem solving refers to cognitive processing directed at achieving a
goal when the problem solver does not initially know a solution method
(Richard E. Mayer).
When someone has a goal but does not know how to solve it that’s
called a problem, so that you have to solve that problem in any way to
reach the result that make you satisfied.
Problem solving, especially in business, is a complicated science. Not only are
business conflicts multifaceted, but they often involve different personalities. In
recent years, however, there has been a rise in psychology-driven problem
solving techniques. [2]
In psychology it refers to the process of finding solutions to problems
encountered in life, and in engineering it used when products or processes fail,
so corrective action can be taken to prevent further failures .[3]
Steps in Solving a Problem:
It is agreed that first step to solve a problem, is defining the problem, identify the
key factors and actors, generate possible solutions, and then evaluate them to
pick the best option. [2]
Problem solving strategies and methods are the steps to find your solution.
3
Problem Solving Strategies:
To avoid that you don’t fall victim to the same challenges in the future, Problem
solving strategies and methods are the steps that one would use to find the
problems and its best solution.
Developing new strategies and methods help in organizing and fixing the
problems.
Also creative problem solving methods that you can use to identify challenges,
create actionable goals, and resolve problems as they arise. Although there is
often procedural and objective crossover among techniques, they are grouped by
theme so you can identify which method works best for your organization. [2]
These are some of problem solving techniques and strategies:
1. Brainstorming: One of the most common methods of divergent
thinking, it happen when a large group of people share their
thoughts and creative ideas together. The goal is to generate as
many ideas as possible. [2]
2. Abstraction: problem solving techniques to Change Perspective to
solve the problem in a model of the system before applying it to the
real system.
3. Lateral Thinking: “Lateral thinking is solving problems through an
indirect and creative approach, using reasoning that is not
immediately obvious and involving ideas that may not be obtainable
by using only traditional step-by-step logic.” [1]
4. Root Cause Analysis: it is a strategies for problem cause
identification, This method helps identify the most critical cause of a
problem.[2]
4
Problem Solving Methods:
1. DEMING-SHEWHART CYCLE: PLAN-DO-CHECK-ACT (PDCA):
(Process-Oriented Problem Solving Methods). [2]
Named for W. Edwards Deming and Walter A. Shewhart, The PDSA cycle
is also used to illustrate a quality improvement method that uses data as
the basis for making decisions. [5]
This model follows a four step process: [4]
 Plan: Establish goal and process required to start deliver the result
you want.
 Do: implement and doing the solution.
 Check: check and test the solution.
 Act/Adjust: If different results have been seen in the test process,
then adjust accordingly.
2. 8D PROBLEM-SOLVING:
It is a method developed at Ford Motor Company used to approach and to
resolve problems.
In the manufacturing sector, the 8D process is almost a de facto standard
and unique in its origin with the customer. [6]
Its goal is to introduce a fast fix in the short term while working on a more
permanent solution with no recurring issues. [4]
8D problem solving methodology: [6]
1. Select an appropriate team.
2. Formulate the problem definition.
3. Active interim containment.
4. Find root causes.
5. Select and validate corrective actions.
6. Take preventive steps.
7. Congratulate the team
5
3. TRIZ:
TRIZ is the Russian-developed problem solving technique translated to
“Theory of Inventive Problem Solving” or TIPS in English.
It is a problem solving based on data or logic, which make the team to
develop creative work in the fastest ways. Also it is an international
science that depends on pattern of problems and solutions. [7]
Whose method is best? How to choose the method that fit my problem?
Solving a problem required some knowledge of your problem topic or, has some
old experience. When choosing your problem you can search for the method,
which make your solution optimal and unique with best save of time or money or
effort. So choosing any of the methods or strategies won’t make big problem.
C-Travel Agent as Search problem ;
In Artificial intelligent Searching is an important technique in solving problems.
Problem Solving agents can lead to wanted states by finding sequence of actions
being deciding from those goal based agents.
As for the first step we have goal formulation in the problem solving then problem
formulation that decides actions and states. To find the unknown value we go
through sequence of actions and decide the best ones this is called search . the
environment can be seen within 4 types static , observable, discrete and
deterministic.
There are four different types of problems :
1. Single state problems : fully observable and deterministic.
2. Multiple states problems : Non-observable and deterministic.
3. Contingency problems : non-deterministic and partially observable.
4. Exploration problems : Unknown state space.
A problem is an information gathering that the Agent is going to use this to
decide what to do and it is defined by 5 components :
1. Initial state.
2. Actions available to the agent.
3. Transition model
6
4. Goal test
5. Path cost function
Search strategy is related to the node expansion they are evaluated by
completeness , Optimality , Time complexity, Space Complexity . types of search
strategies are Uninformed search , Informed search , optimization and Game
playing. There six uninformed search strategies : Breadth-first , Uniform-cost,
Depth-first, Depth limited search , iterative deepening and bidirectional search .
there two informed search : best first search and A* Search.
Travel agent is considered as search problem because User go through
sequence of different actions as in searching for suitable time to fly from starting
city to destination city choosing most optimal time for him.
I. System components are Search , user interface and access database.
(Using python Language)
As in Search using A* Search :
def As_Searching(departure, destination, Ttime, SpaceTime, Frange, Olist):
 if departure == destination:
 for i in range(len(Olist)):
 print("Deparcure from "+ Olist[i][0] +" to "+Olist[i][1]+" on "+ Olist[i][2] +
"in Dayes " + Olist[i][3] + " : " + Olist[i][4])
 return
 Dcity = GetCity(departure,listOfcity)
 listOfcity.remove(dcity)
 edges = GetTimeT(dcity,ListeOftime)
 dummyHeuristic = 1000
 suitableDay = None
 suitableDepart = None
 suitableArr = None
 suitableTable = None
 for i in range(len(edges)):
 flightsList = edges[i].Flights
 foundedList = CheckDay(Frange,flightsList)
 if len(foundedList) > 0:
 Spacival = check_SpaceTime(foundedList,SpaceTime)
 if len(Spacival) > 0:
 Ncity = GetCity(edges[i].city2,listOfcity)
 if Ncity.name == departure:
 heuristic = Data1.calculateTime(Spacival[1],Spacival[2])
7
 else:
 heuristic = Data1.calculateDistance(dcity,Ncity) +
Data1.calculateTime(Spacival[1],Spacival[2])
 if heuristic < dummyHeuristic:
 dummyHeuristic = heuristic
 suitableDay = Spacival[0]
 suitableTable = edges[i]
 suitableDepart = Spacival[1]
 suitableArr = Spacival[2]
A* search Combines both Greedy search and uniform Cost Search to
have complete and optimal Algorithm to find path and graph traversals.
In this method we calculate time and distance to find the best solution.
As for User interface :
from data import Data
from planner_engine import A_star
start=input("enter start city: ")
dest=input("enter destination city: ")
list=input("enter travel day: ").split()
Flight11 = Data.Flight1
Flight22 = Data.Flight2
City1 = Data.City1
City2 = Data.City2
A_star(start,dest,list)
In this method we take the input from user, the city he is travelling to and the day
of flights he want to travel on .
As for Data Access :
import pandas as pd
xl=pd.ExcelFile("Travel Agent KB (2 sheets).xlsx")
df=xl.parse('Flights')
print(df)
in this method we access data from excel sheet that contain name of the cities
and flights by importing this sheet to the code.
8
References:
1. 4 Problem Solving Techniques: How to Solve Problems at Work. (2020).
Retrieved 15 May 2020, from https://www.thevectorimpact.com/problemsolving-techniques/
2. Definitive Guide to Problem Solving Techniques | Smartsheet. (2020).
Retrieved 15 May 2020, from https://www.smartsheet.com/problemsolving-techniques
3. Jerrold R. Brandell (1997). Theory and Practice in Clinical Social Work.
Simon and Schuster. p. 189. ISBN 978-0-684-82765-0.
4. The Ultimate Problem-Solving Process Guide: 31 Steps and Resources.
(2020). Retrieved 15 May 2020, from
https://www.initiativeone.com/insights/blog/problem-solving-process/
5. (2020). Retrieved 16 May 2020, from
https://jolt.merlot.org/Vol11no2/Gazza_0615.pdf
6. Introduction to 8D Problem Solving. (2020). Retrieved 16 May 2020, from
https://books.google.com.eg/books?hl=ar&lr=&id=CjUqDwAAQBAJ&oi=fn
d&pg=PT3&dq=Introduction+To+8D+Problem+Solving:+Including+Practic
al+Applications+and+Examples&ots=JKQl9aO7KF&sig=6Hf1AKyUwjpJoK
7XXSy24e26DoA&redir_esc=y#v=onepage&q=Introduction%20To%208D
%20Problem%20Solving%3A%20Including%20Practical%20Applications
%20and%20Examples&f=false
7. Barry, K., Domb, E., & S. Slocum, M. (2020). TRIZ - What Is TRIZ?.
Retrieved 16 May 2020, from
https://web.archive.org/web/20100926070709/http://www.trizjournal.com/archives/what_is_triz/
