from statemachine import StateMachine, State


class basicFSM(StateMachine):
    Start = State('Start', initial=True)
#    Idle = State('Idle', initial=True)
    Idle = State('Idle')
    Next = State('Next')
    Full = State('Full')
    
    initial =  Start.to(Idle) 
    hit = Idle.to(Next)
    dig = Next.to(Idle)
    full = Next.to(Full)
    rst = Full.to(Start) 



