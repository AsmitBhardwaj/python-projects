public abstract class Operator{
    
    
    //This returns the precedence of the operator
    public abstract int getPrecedence();
    
    //this method evaluates the operator using the two operands given
    public abstract double evaluate(double a, double b);
}
    
    
