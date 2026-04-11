class ExpOperator extends Operator{
    
    @Override
    //Exponent has a precedence level of 3
    public int getPrecedence(){
        return 3;
    }
        
    //this method will evaluate the entered inputs
    public double evaluate(double a, double b){
        return Math.pow(a,b);
    }
}
    
