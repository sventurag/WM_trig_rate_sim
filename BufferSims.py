from statemachine import StateMachine, State



class basicFSM(StateMachine):
    Idle = State('Idle', initial=True)
    Next = State('Next')
    Full = State('Full')

    hit = Idle.to(Next)
    dig = Next.to(Idle)
    full = Next.to(Full) 


