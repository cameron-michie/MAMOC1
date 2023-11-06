
using ReactionDiffusion;

Console.WriteLine("Hello world!");

int gridxsize = 100;
int gridysize = 100;

double Prey_E0 = 200;
double Prey_EP = 10;
int Prey_N = 600;

double Pred_E0 = 200;
double Pred_EP = 10;
int Pred_N = 220;

Grid TheGrid = new Grid(gridxsize, gridysize);
Species Prey = new Species("Prey", Prey_E0, Prey_EP, Prey_N, TheGrid);
Species Pred = new Species("Pred", Pred_E0, Pred_EP, Pred_N, TheGrid);

for (int i = 0 ; i < 1000; i++) 
{
    //Console.WriteLine($"{i}     Prey: {Prey.AgentsList.Count}   Pred : {Pred.AgentsList.Count}");
    Prey.Move();
    Pred.Move();
    TheGrid.Interact(Prey, Pred);
}

