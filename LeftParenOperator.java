public class LeftParenOperator extends Operator{
    
    public int getPrecedence(){
        //it has the lowest precedence as well so that nothing happens until the right parenthesis comes up
        return 0;
    }
    
    //throw exception
    public double evaluate(double a, double b){
        throw new UnsupportedOperationException();
    }
}