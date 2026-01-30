public class AddOperator extends Operator{
    
    @Override
    //addition and subtraction have precedence 1
    public int getPrecedence(){
        return 1;
    }
    
    public double evaluate(double a, double b){
        return a+b;
    }
}
