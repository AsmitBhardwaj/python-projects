public class DivOperator extends Operator{
    
    @Override
    //multiplication and division have precedence of 2
    public int getPrecedence(){
        return 2;
    }
    
    //evaluate method to divide the entered inputs
    public double evaluate(double a, double b){
        return a/b;
    }
}
    
        
