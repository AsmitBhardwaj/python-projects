import java.util.Stack;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;
import javafx.geometry.Insets;


public class Calculator extends Application{
    
    //the calculator dimensions
    public static int CALC_WIDTH = 300;
    public static int CALC_HEIGHT = 200;
    
    //adding opereator and operand data members
    private Stack<Double> operandStack = new Stack<>();
    private Stack<Operator> operatorStack = new Stack<>();
    
    //holds the current number being built from the press of the button
    private String currentNumber = "";
    
    //the calculator screen
    private TextField screen;
    
    //the calculator buttons
    private Button button0;
    private Button button1;
    private Button button2;
    private Button button3;
    private Button button4;
    private Button button5;
    private Button button6;
    private Button button7;
    private Button button8;
    private Button button9;
    private Button buttonLeftParen;
    private Button buttonRightParen;
    private Button buttonAdd;
    private Button buttonSub;
    private Button buttonMul;
    private Button buttonDiv;
    private Button buttonClear;
    private Button buttonDot;
    private Button buttonEqual;
    private Button buttonExp;
    
    /**
     * This method will append digits to the number that is being built from the number presses
     * **/
    private void appendDigit(String digit){
        //add digit to the number
        currentNumber += digit;
        
    }
    
    public static void main(String[] args){
        launch(args);
    }
    
    @Override
    public void start(Stage primaryStage){
        //create calculator screen
        screen = new TextField();
        
        //creating buttons
        button1 = new Button("1");
        button2 = new Button("2");
        button3 = new Button("3");
        button4 = new Button("4");
        button5 = new Button("5");
        button6 = new Button("6");
        button7 = new Button("7");
        button8 = new Button("8");
        button9 = new Button("9");
        button0 = new Button("0");
        buttonLeftParen = new Button("(");
        buttonRightParen = new Button(")");
        buttonAdd = new Button("+");
        buttonSub = new Button("-");
        buttonMul = new Button("x");
        buttonDiv = new Button("/");
        buttonClear = new Button("C");
        buttonDot = new Button(".");
        buttonEqual = new Button("=");
        buttonExp = new Button("^");
        
        //attach handler to process clicks
        ButtonHandler handler = new ButtonHandler();
        button1.setOnAction(handler);
        button2.setOnAction(handler);
        button3.setOnAction(handler);
        button4.setOnAction(handler);
        button5.setOnAction(handler);
        button6.setOnAction(handler);
        button7.setOnAction(handler);
        button8.setOnAction(handler);
        button9.setOnAction(handler);
        button0.setOnAction(handler);
        buttonLeftParen.setOnAction(handler);
        buttonRightParen.setOnAction(handler);
        buttonAdd.setOnAction(handler);
        buttonSub.setOnAction(handler);
        buttonMul.setOnAction(handler);
        buttonDiv.setOnAction(handler);
        buttonClear.setOnAction(handler);
        buttonDot.setOnAction(handler);
        buttonEqual.setOnAction(handler);
        buttonExp.setOnAction(handler);
                                
        
        //set up a grid panel for the keyboard
        GridPane keypad = new GridPane();
        keypad.setMinSize(CALC_WIDTH, CALC_HEIGHT);
        keypad.setPadding(new Insets(10, 10, 10, 10));
        keypad.setVgap(5);
        keypad.setHgap(5);
        keypad.setAlignment(Pos.CENTER);
        
        //attach the buttons to the keypad grid
        //have different columns and rows for each button
        //row 0 will have 1, 2, 3, +, -
        keypad.add(button1, 0, 0);
        keypad.add(button2, 1, 0);
        keypad.add(button3, 2, 0);
        keypad.add(buttonAdd, 3, 0);
        keypad.add(buttonSub, 4, 0);
        
        //row 1 will have 4, 5, 6, *, /
        keypad.add(button4, 0, 1);
        keypad.add(button5, 1, 1);
        keypad.add(button6, 2, 1);
        keypad.add(buttonMul, 3, 1);
        keypad.add(buttonDiv, 4, 1);
        
        //row 2 will have 7, 8, 9, (, )
        keypad.add(button7, 0, 2);
        keypad.add(button8, 1, 2);
        keypad.add(button9, 2, 2);
        keypad.add(buttonLeftParen, 3, 2);
        keypad.add(buttonRightParen, 4, 2);
        
        //row 3 will have 0, ., =, ^, C
        keypad.add(button0, 0, 3);
        keypad.add(buttonDot, 1, 3);
        keypad.add(buttonEqual, 2, 3);
        keypad.add(buttonExp, 3, 3);
        keypad.add(buttonClear, 4, 3);
        
        
        //put screen and keypad together
        BorderPane gui = new BorderPane();
        gui.setTop(screen);
        gui.setCenter(keypad);
        
        //set up the scene
        Scene scene = new Scene(gui);
        primaryStage.setTitle("Calculator");
        primaryStage.setScene(scene);
        primaryStage.show();
        
    }
    
    //handler for processing the button clicks
    private class ButtonHandler implements EventHandler<ActionEvent>{
        
        /**
         * we are going to add number buttons here
         * we are going to call appenddigit method to build the number from the buttons being pressed
         */ 
        
        @Override
        public void handle(ActionEvent e){
            //numbers
            if(e.getSource() == button1){
                appendDigit("1");
                screen.appendText("1");
            }
            else if(e.getSource() == button2){
                appendDigit("2");
                screen.appendText("2");
            }
            else if(e.getSource() == button3){
                appendDigit("3");
                screen.appendText("3");
            }
            else if(e.getSource() == button4){
                appendDigit("4");
                screen.appendText("4");
            }
            else if(e.getSource() == button5){
                appendDigit("5");
                screen.appendText("5");
            }
            else if(e.getSource() == button6){
                appendDigit("6");
                screen.appendText("6");
            }
            else if(e.getSource() == button7){
                appendDigit("7");
                screen.appendText("7");
            }
            else if(e.getSource() == button8){
                appendDigit("8");
                screen.appendText("8");
            }
            else if(e.getSource() == button9){
                appendDigit("9");
                screen.appendText("9");
            }
            else if(e.getSource() == button0){
                appendDigit("0");
                screen.appendText("0");
            }
            else if(e.getSource() == buttonDot){
                appendDigit(".");
                screen.appendText(".");
            }
            
            //maths operators
            else if(e.getSource() == buttonAdd){
                processOperator(new AddOperator());
                screen.setText(screen.getText() + "+");
            }
            else if(e.getSource() == buttonSub){
                processOperator(new SubOperator());
                screen.setText(screen.getText() + "-");
            }
            else if(e.getSource() == buttonMul){
                processOperator(new MulOperator());
                screen.setText(screen.getText() + "*");
            }
            else if(e.getSource() == buttonDiv){
                processOperator(new DivOperator());
                screen.setText(screen.getText() + "/");
            }
            else if(e.getSource() == buttonExp){
                processOperator(new ExpOperator());
                screen.setText(screen.getText() + "^");      
            }
            
            //special buttons
            else if(e.getSource() == buttonEqual){
                processOperator(new EqualsOperator());
                if(!operandStack.isEmpty()){
                    screen.setText(String.valueOf(operandStack.peek()));
                    currentNumber = "";
                }
            }
            else if(e.getSource() == buttonClear){
                currentNumber = "";
                operandStack.clear();
                operatorStack.clear();
                screen.setText("");
                
            }
            else if(e.getSource() == buttonLeftParen){
                processOperator(new LeftParenOperator());
                screen.setText(screen.getText() + "(");
        }
            else if(e.getSource() == buttonRightParen){
                processOperator(new RightParenOperator());
                screen.setText(screen.getText() + ")");
            }
        }
    }
        
        
        /**
         *helper method to perform the top most calculation of the stack
         *pops one operator and two operands
         */
        private void evaluateTop(){
            //operator with highest precedence will be evaluated first
            Operator op = operatorStack.pop();
            
            //the first number will be second operand and second number will be first operand cos of LIFO
            double num2 = operandStack.pop();
            double num1 = operandStack.pop();
            
            //evaluate oit
            double result = op.evaluate(num1, num2);
            
            //push the result to the operand stack
            operandStack.push(result);
        }
    
            
        
        
        /**
         * Mehtod to process the operator entered by the user
         */
        private void processOperator(Operator currOp){
        
            //convert the string and push it to the operand stack
            if(!currentNumber.equals("")){
                operandStack.push(Double.parseDouble(currentNumber));
                currentNumber = "";
            }
            
            //handle right parentheses
            if(currOp instanceof RightParenOperator){
                //evaluate everything until left parenthesis
                while(!(operatorStack.peek() instanceof LeftParenOperator)){
                    evaluateTop();
                }
                
                //remove left parenthesis from stack
                operatorStack.pop();
            }
            
            //we will always push parentheses
            else if(currOp instanceof LeftParenOperator){
                operatorStack.push(currOp);
            }
            
            //while top of stack has higher or equal precedence, we will evaluate it
            //we will check if the stack is not empty and the precedence of the curr is more
            else{
                while(!operatorStack.isEmpty() && operatorStack.peek().getPrecedence() >= currOp.getPrecedence()){
                    //call evaluateTop method
                    evaluateTop();
                }
            
                    //operators with 0 precedence are not stored but the left parentheses is stored even tho its precedence is 0
                if(currOp.getPrecedence() > 0 || currOp instanceof LeftParenOperator){
                    operatorStack.push(currOp);
        
                }
            }
        }
}


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        