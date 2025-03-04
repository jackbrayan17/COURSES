### **6.1 Knowledge-Based Agents**

A **knowledge-based agent** is an intelligent agent that makes decisions based on knowledge represented in a structured form, typically through logical statements or symbols. These agents reason about the world using this knowledge to take actions that are likely to achieve their goals.

**Key Components of Knowledge-Based Agents:**

1. **Knowledge Base (KB):** A collection of facts and rules representing the agent’s knowledge about the world.
2. **Inference Mechanism:** A system for deriving new knowledge from existing facts and rules in the KB.
3. **Agent’s Architecture:** The hardware and software components that allow the agent to perceive its environment, perform reasoning, and take actions based on its conclusions.

**Example:**  
A robot in a warehouse might have knowledge about the layout of the warehouse, the location of products, and the task of fetching a specific product. It reasons about the best path to take and uses its knowledge base to perform its task efficiently.

---

### **6.2 The Wumpus World**

The **Wumpus World** is a classical environment used to demonstrate knowledge-based agents. It consists of a grid with various elements:

1. **Wumpus:** A dangerous creature that kills the agent if it is in the same square.
2. **Pit:** A trap that causes the agent to fall and die.
3. **Gold:** An item the agent needs to find and retrieve.
4. **Agent’s Actions:** Move, turn, grab gold, shoot an arrow (to kill the Wumpus).

The agent perceives the environment through sensors:

- **Breeze:** Detected if there is a pit in a neighboring square.
- **Stench:** Detected if the Wumpus is in a neighboring square.
- **Glitter:** Detected if the agent is in the same square as the gold.

The agent’s objective is to find the gold, avoid the Wumpus and pits, and then exit the world. The agent uses its **knowledge base** to deduce safe moves, identify the presence of the Wumpus or pits, and avoid dangerous areas.

---

### **6.3 Logic**

**Logic** is a formal system of reasoning used to represent and manipulate knowledge. In AI, logic provides a structured way for agents to reason about the world and make decisions.

**Types of Logic:**

1. **Propositional Logic:** Deals with simple statements that are either true or false (e.g., "It is raining").
2. **First-Order Logic (Predicate Logic):** Allows for more expressive statements, including quantifiers and predicates (e.g., "John is a student" or "Every student has a book").
3. **Modal Logic:** Incorporates concepts of necessity and possibility (e.g., "It is necessary that...").

**Logic Systems in AI:**

- **Declarative knowledge representation**: Facts and rules about the world.
- **Inference**: The process of drawing conclusions from knowledge using logical rules.

---

### **6.4 Propositional Logic: A Very Simple Logic**

**Propositional Logic (PL)** is a simple form of logic where statements (propositions) can either be true or false. Propositions are connected by logical connectives, such as:

- **AND (∧):** Both propositions must be true.
- **OR (∨):** At least one proposition must be true.
- **NOT (¬):** The negation of a proposition (if A is true, then ¬A is false).
- **IMPLIES (→):** If one proposition is true, then another proposition must also be true.

**Syntax of Propositional Logic:**

- **Atoms**: Basic propositions, such as "It is raining" (represented as PP).
- **Compound Statements**: Combinations of atoms using logical connectives, such as P∧QP \land Q (It is raining and it is cold).

**Truth Tables:**  
Truth tables are used to evaluate the truth values of compound statements based on the truth values of the individual propositions.

**Example:**  
Given the propositions:

- PP: "It is raining"
- QQ: "I will take an umbrella"  
    The statement "If it is raining, then I will take an umbrella" is written as P→QP \rightarrow Q.

---

### **6.5 Propositional Theorem Proving**

**Theorem proving** in propositional logic refers to the process of determining whether a given logical expression (theorem) can be derived from a set of axioms or premises.

**Methods of Theorem Proving:**

1. **Truth Table Method:** A brute-force approach that evaluates all possible combinations of truth values for the variables involved.
2. **Resolution:** A more efficient method that refines a logical expression until a contradiction is found or a solution is derived.

**Example:**  
To prove a theorem in propositional logic, such as (P∧Q)→R(P \land Q) \rightarrow R, we would attempt to derive RR from PP and QQ using rules of inference.

---

### **6.6 Efficient Propositional Model Checking**

**Model checking** is a technique used to verify whether a model (or a logical system) satisfies certain properties. In propositional logic, this involves checking whether a particular formula holds true in a given model (a specific assignment of truth values to variables).

**Efficiency Concerns:**

- **State Explosion Problem:** The number of possible models grows exponentially with the number of variables.
- **Techniques to improve efficiency:**
    - **Symbolic Model Checking**: Uses symbolic representations to compactly store information about models.
    - **Binary Decision Diagrams (BDDs):** A data structure that efficiently represents Boolean functions.

**Example:**  
To verify whether a propositional logic formula holds true in a large system (e.g., in a scheduling system), model checking can be used to check all possible states of the system.

---

### **6.7 Logic-Based Agents**

**Logic-based agents** use logic to represent knowledge and perform reasoning. They are built around a **knowledge base (KB)** and an **inference engine**. These agents use logical reasoning to derive new facts, make decisions, and take actions.

**Components of Logic-Based Agents:**

1. **Knowledge Base (KB):** A repository of facts and rules about the environment.
2. **Inference Engine:** A system that performs reasoning based on the KB.
3. **Decision Making:** The agent uses logical reasoning to decide what actions to take, often using **deductive reasoning** (deriving specific conclusions from general facts).

**Example:**  
In the Wumpus World, a logic-based agent would have a KB that includes facts about the layout of the world and the agent's observations. Using logical inference, the agent deduces the safest path and takes actions to achieve its goal of finding and retrieving the gold.

---

### **Exercises**

1. **Wumpus World Knowledge Base:** Write the knowledge base for a Wumpus World agent with at least 3 squares, including information about the agent’s location, the Wumpus, and the pits.
2. **Propositional Logic:** Given the propositions PP, QQ, and RR, construct a truth table for the compound statement P∧(Q→R)P \land (Q \rightarrow R).
3. **Theorem Proving:** Prove the following logical statement using truth tables: (P∨Q)→(P∨Q)(P \lor Q) \rightarrow (P \lor Q).
4. **Model Checking:** Using a propositional logic formula, simulate a model checking process to see if a given formula holds true in a specific model.
5. **Logic-Based Agent:** Design a simple logic-based agent that can solve a basic puzzle (e.g., a simplified Wumpus World or Sudoku) using reasoning and inference.
