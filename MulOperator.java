public class MulOperator extends Operator{
    
    @Override
    //multiplication and division have precedence of 2
    public int getPrecedence(){
        return 2;
    }
    
    //method to evaluate the multiplication of the entered inputs
    public double evaluate(double a, double b){
        return a*b;
    }
}

