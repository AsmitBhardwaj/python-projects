public class EqualsOperator extends Operator{
    
    //as mentioned in class, equals has the lowest precedence of all the operators since it is the last operator we will be evaluating
    public int getPrecedence(){
        return 0;
    }
    
    //throw UnsupportedOperationException
    public double evaluate(double a, double b){
        throw new UnsupportedOperationException();
    }
}

        
