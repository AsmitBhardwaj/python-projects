public class RightParenOperator extends Operator{
    
    public int getPrecedence(){
    //ignored until its pushed from the stack
        return 0;
    }
    
    //throw exception
    public double evaluate(double a, double b){
        throw new UnsupportedOperationException();
    }
}
