### **12.1 Acting in Uncertainty**

**Acting under uncertainty** is a fundamental challenge in AI. In the real world, agents often need to make decisions without knowing all the relevant information or when outcomes are not deterministic. The ability to model and act under uncertainty allows intelligent systems to make rational decisions even in the face of incomplete knowledge.

#### Key Concepts:

- **Uncertainty:** Refers to the lack of information about the environment or the future. This can arise due to factors such as incomplete knowledge, probabilistic events, or non-deterministic actions.
- **Decision Making under Uncertainty:** An agent must evaluate different possible outcomes and choose actions that maximize its expected utility, given the uncertainty.
- **Types of Uncertainty:**
    - **Aleatoric Uncertainty:** Due to randomness or inherent variability in the environment.
    - **Epistemic Uncertainty:** Due to lack of knowledge or information about the environment.

#### Example:

In a medical diagnosis system, uncertainty arises when the system does not know whether a patient truly has a particular disease based on the symptoms and test results.

---

### **12.2 Basic Probability Notation**

Probability theory provides a framework for quantifying uncertainty. It allows for representing uncertainty as numerical values between 0 and 1, where 0 means an event will not occur, and 1 means it will certainly occur.

#### Key Concepts:

- **Random Variables:** Denoted by capital letters (e.g., XX), representing the outcomes of random phenomena.
- **Probability Distribution:** Describes the likelihood of different outcomes for a random variable. For example, P(X=x)P(X = x) represents the probability that the random variable XX takes the value xx.
- **Conditional Probability:** The probability of an event occurring given that another event has occurred. Denoted as P(A∣B)P(A | B), the probability of AA given BB.
- **Joint Probability:** The probability of two or more events occurring together, denoted as P(A∩B)P(A \cap B).

#### Example:

If XX represents the outcome of rolling a fair die, then P(X=4)=16P(X = 4) = \frac{1}{6}, as each outcome on a fair die has equal probability.

---

### **12.3 Inference Using Complete Joint Distributions**

In many AI systems, it is necessary to reason about multiple variables at the same time. A **joint distribution** describes the probability of two or more variables occurring together.

#### Key Concepts:

- **Joint Probability Distribution:** A distribution that specifies the probability of different combinations of values for multiple variables. For example, for two variables XX and YY, the joint probability distribution P(X,Y)P(X, Y) represents the probability of every possible combination of XX and YY.
- **Marginalization:** To obtain the probability distribution of one variable by summing or integrating over the possible values of other variables in the joint distribution. For example, P(X)=∑YP(X,Y)P(X) = \sum_{Y} P(X, Y).
- **Conditional Probability from Joint Distribution:** Given a joint distribution, you can calculate conditional probabilities. For example, P(X∣Y)=P(X,Y)P(Y)P(X | Y) = \frac{P(X, Y)}{P(Y)}.

#### Example:

Given the joint probability distribution for two variables XX and YY, you can compute the probability that XX occurs given YY by summing over the possible values of YY.

---

### **12.4 Independence**

Two events or variables are said to be **independent** if the occurrence of one does not affect the probability of the other.

#### Key Concepts:

- **Independence of Variables:** If two variables XX and YY are independent, then P(X,Y)=P(X)P(Y)P(X, Y) = P(X)P(Y). This means that the joint probability is simply the product of the individual probabilities.
- **Conditional Independence:** Variables XX and YY are conditionally independent given a third variable ZZ if P(X,Y∣Z)=P(X∣Z)P(Y∣Z)P(X, Y | Z) = P(X | Z) P(Y | Z).

#### Example:

In a dice-rolling game, the outcome of the first die roll is independent of the outcome of the second die roll, meaning P(A,B)=P(A)P(B)P(A, B) = P(A)P(B), where AA and BB are the results of the two dice.

---

### **12.5 Bayes' Rule and its Use**

**Bayes' Rule** provides a way to update the probability of a hypothesis based on new evidence. It is a powerful tool in probabilistic reasoning, widely used in machine learning, decision making, and diagnostic systems.

#### Bayes' Rule Formula:

P(H∣E)=P(E∣H)P(H)P(E)P(H | E) = \frac{P(E | H) P(H)}{P(E)}

Where:

- P(H∣E)P(H | E) is the **posterior probability**, or the probability of hypothesis HH given the evidence EE.
- P(E∣H)P(E | H) is the **likelihood**, or the probability of observing the evidence EE given the hypothesis HH.
- P(H)P(H) is the **prior probability**, or the probability of the hypothesis before seeing the evidence.
- P(E)P(E) is the **marginal likelihood**, or the total probability of observing the evidence across all hypotheses.

#### Example:

In medical diagnosis, Bayes' Rule can be used to update the probability that a patient has a particular disease given new test results.

---

### **12.6 The Wumpus World Revisited**

The **Wumpus World** is a classic problem in AI that involves an agent navigating a grid-like world with hazards, such as pits and a dangerous creature called the Wumpus. The agent must make decisions under uncertainty and use probabilistic reasoning to act safely.

#### Key Concepts:

- **Stochastic Environment:** The Wumpus World is non-deterministic, meaning that certain actions (like moving or shooting an arrow) may have unpredictable outcomes.
- **Uncertainty in Sensing:** The agent receives noisy or incomplete sensor readings. For instance, it might smell a hint of the Wumpus' presence but can't be certain of its exact location.
- **Bayesian Updating:** In this world, the agent can use Bayesian inference to update its belief about the locations of hazards as it receives more sensory information.

#### Example:

The agent might move forward based on its current belief about the Wumpus' location, and then, after sensing a breeze (indicating a pit nearby), it updates its belief about where the pits are located.

---

### **Exercises**

1. **Bayesian Inference Exercise:** In the context of diagnosing a disease, suppose there is a test for the disease that is 95% accurate (i.e., it correctly identifies diseased patients 95% of the time). If 1% of the population has the disease, what is the probability that a patient has the disease given a positive test result using Bayes' Rule?
    
2. **Joint Probability Distribution Exercise:** Consider two random variables: XX (weather) with possible values "Rainy" and "Sunny," and YY (umbrella) with possible values "Yes" and "No." Given the joint probability distribution P(X,Y)P(X, Y), calculate the marginal distribution P(X)P(X) and the conditional probability P(Y∣X)P(Y | X).
    
3. **Independence Exercise:** In a medical study, the probability of having a headache is 0.3, and the probability of having a cold is 0.4. If these events are independent, calculate the probability of having both a headache and a cold.
    
4. **Wumpus World Exercise:** In the Wumpus World, the agent has sensory information indicating a breeze in two adjacent squares. How can the agent use probabilistic reasoning to infer the presence of a pit in those squares? What strategies would the agent use to safely navigate the world?
    