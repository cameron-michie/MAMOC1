# **_MAMOC1 _**


## Introduction

Theoretical ecology is a mathematical framework for understanding how the interactions of individual organisms with each other and with the environment determine the distribution of populations and the structure of communities. Many different models are needed, each based on some set of hypotheses about the scale and structure of the spatial environment and the way that organisms disperse through it. When many agents interact in simple ways, sometimes emergent properties can be observed in their collective, such as the propagation of wavefronts or the formation of patterns. 

Reaction-diffusion models are a way of translating the simple assumptions about ways agents can move and interact on the local level into global conclusions about the persistence or extinction of populations and the coexistence of interacting species. Born from the macroscopic observations of molecular diffusion, reaction-diffusion models now more widely refer to any event-driven system of interacting moving agents. In biology, the great success of reaction-diffusion is the Turing model, which describes how homogeneous groups of cells in an embryo can spontaneously differentiate into patterns, like the spots and stripes on animal skins. In chemistry, the Belousov-Zhabotinsky chemical reaction displays incredible dispersive concentric patterns. Further examples are as distributed as econometric information diffusion, as  and as grievous as modelling the spread of forest fires. 


## Mathematics of Reaction-Diffusion Systems

The general form of reaction-diffusion differential equation systems is given by 

$$\delta_{t} q_{i} =  D_{m,n} \nabla^{2} q_{i} + R_{j}(q_{j})   $$

where $$q_{i}$$ describes a concentration, $$D_{m,n}$$ the diffusion coefficient, and $$R_{j}(q_{j})$$ a function of concentration representing agents local behaviour - i.e. the birth and death rate of the agents. The first term on the right hand side can be recognised as Fick’s law.

The dynamics of our model is specified by the rates at which individuals move and die or reproduce. As such, a good place to start is to consider the local mechanics of our agent movement and reactions, supposing that agents may only move to a randomly chosen nearest neighbour of their location, and reproduce or die at rates which depend on the number of individuals at the same location. Using some simplifying assumptions along the way, there are creative ways to derive the reaction term, which is usually, hopefully, linear in $$q_i$$. Often, however, we are not so lucky. Spatial models often unavoidably invite non-linear terms, resulting in chaotic long-term behaviour.


## Predator-Prey models


### Lotka-Volterra equations.

The non-spatial Lotka-Volterra model lets us explore the reaction terms for a basic diffusion-reactive system. Since we want to completely ignore spatial dimensions, we can use the mean field assumption: that all agents interact with the average effect of all others. Letting $$( x_1(t) $$ denote the prey population and $$x_2(t) $$ denote the predator population at time $$t $$, we get

$$ \frac{dx_1}{dt} = \alpha x_1 - \beta x_1 x_2 $$,

$$ \frac{dx_2}{dt} = \delta x_1 x_2 - \gamma x_2 $$.

Here:

- $$ \alpha $$is the natural birth rate of the prey in the absence of predators.

- $$ \beta $$ is the death rate of the prey due to predation.

- $$ \gamma $$ is the natural death rate of the predators in the absence of prey.

- $$\delta $$ is the rate at which predators increase by consuming prey.

The steady states of this system of differential equations are found by setting the time derivatives to zero. The trivial solution $$ x_1 = x_2 = 0$$ indicates mutual extinction, but otherwise, solving for constants, we get $${x_1, x_2} = {\gamma / \delta, \alpha / \beta}$$. We would like to analyse the stability of these steady state solutions. To do this, we linearise our set of differential equations, so that we have

$$ \delta_{t}$$_{i} = J_{m,n} (x_{i}) x_{i} = \alpha - \beta x_2 & - \beta x_1\\ \delta x_2 & \delta x_1 - \gamma x_i $$

Subbing in our values for $$x_1$$ and $$x_2$$ gives us the matrices … The first has eigenvalue $$\alpha$$ and $$-\gamma$$, indicating a saddle point. This is good, because saddle points are unstable, meaning the model does not predict spiralling uncontrollably towards extinction. The other matrix has eigenvalues $$i \sqrt{\alpha \gamma}$$ and $$- i \sqrt{\alpha \gamma}$$, which indicates periodic trigonometric-esque solutions.

//// Insert photo of population in typical lotka volterra

The model elegantly captures the core ideas: prey populations grow naturally but are eaten by predators, and predator populations decline without food but grow when they eat prey.

Adding in our Fick’s law inspired diffusion terms, we get the spatial Lotka-Volterra equations 

$$\frac{\partial x_1}{\partial t} = \alpha x_1 - \beta x_1 x_2 + D_1 \nabla^2 x_1 $$

$$\frac{\partial x_2}{\partial t} = \delta x_1 x_2 - \gamma x_2 + D_2 \nabla^2 x_2 $$

This set of differential equations can be modelled computationally on a randomised initial population to show the progression of the reaction-diffusion system. This python program 

// insert animation


### Computational agent based models for two species population dynamics.

Spatial ecology can also be modelled computationally without assuming the truth of a set of differential equations using agent-based models. This has been done to some success in the modelling of bacterial biofilms, in financial modelling, in understanding the spread and control of forest fires, in the study of agricultural land use and crop management, in the dynamics of predator-prey systems, and in the prediction of migration patterns and territorial behaviors in wildlife conservation.

Agent based models offer a completely different method for simulating systems of interacting particles by operating exclusively at the local level, with no macroscopic information shared to individual agents. Diffusion occurs via steps in random directions. Reactions occur based on only local information, such as if two interacting agents of the same species at the same place have enough energy to procreate. As a result, these models are much closer approximations to real life simulation.



We assume annie. 


## Turing Pattern Generation
