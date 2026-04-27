# epScript Complete Reference

> Combined reference for epScript (euddraft/eudplib) — StarCraft: Remastered UMS map scripting.
> Language syntax is JavaScript-like. All variables are 32-bit unsigned integers at runtime.
> Use tab indentation in code.

---


---


# epScript Syntax

<br />

- [Basic Syntax](#basic-syntax)
    - [Compile-time And Run-time](#compile-time-and-run-time)
    - [Case Sensitivity](#case-sensitivity)
    - [Value Types](#value-types)
    - [Logical Rules](#logical-rules)
    - [Literal Numbers](#literal-numbers)
    - [Literal Strings](#literal-strings)
    - [Literal Bytes](#literal-bytes)
    - [Naming Rules](#naming-rules)
    - [Importing Other Modules](#importing-other-modules)
    - [Symbols](#symbols)
        - [Code Block {}](#code-block)
        - [Syntax Line Break \;](#syntax-line-break)
        - [Index Operator \[\]](#index-operator)
        - [Assignment Operator \=](#assignment-operator)
        - [Line Comment //](#line-comment)
        - [Block Comment /\* \*/](#block-comment)
        - [Conditional Operator \> \<](#conditional-operator)
        - [Mathematical Operators \+ \- \* \/](#mathematical-operators)
        - [Increment/Decrement/Multiplication/Division Assignment Operators](#incrementdecrementmultiplicationdivision-assignment-operators)
    - [Conditional Statement Syntax](#conditional-statement-syntax)
        - [if](#if)
        - [if else](#if-else)
        - [Conditional Chaining](#conditional-chaining)
        - [Conditional Nesting](#conditional-nesting)
        - [Once Execution](#once-execution)
    - [Control Flow](#control-flow)
        - [for Loop](#for-loop)
        - [while Loop](#while-loop)
        - [break](#break)
        - [foreach Iterator Loop](#foreach-iterator-loop)
        - [switch](#switch)
        - [epdswitch](#epdswitch)

<br />

## Basic Syntax

- ### Compile-time And Run-time

    Any non-compile-time code outside of variable declarations cannot be exposed outside of functions.  
    Functions containing any runtime operations are non-compile-time functions.  
    All variable declaration/initialization/reading/operation/assignment operations are runtime operations.   
    Compile-time code will execute even if the if condition is not met.   


- ### Case Sensitivity

    epScript is a case-sensitive programming language where A and a have different meanings.   


- ### Value Types

    epScript has only one basic `value type`, which is a 32-bit unsigned integer. 


- ### Logical Rules

    Integer `0` is logically false.  
    `Non-zero` integer values are logically true.  


- ### Literal Numbers

    Literal numbers include decimal numbers, hexadecimal numbers, and binary numbers.
    ```JavaScript
    // The following 15, 0xf, and 0b1111 represent the same number 15, just in different ways,
    // so a, b and c are equal.
    var a = 15;
    var b = 0xf; // Hexadecimal numbers start with 0x
    var c = 0b1111; // Binary numbers start with 0b
    ```


- ### Literal Strings

    Literal strings can be enclosed in single quotes `'` or double quotes `"`.  
    ```JavaScript
    DisplayText("This is a literal string");
    DisplayText('This is a literal string');
    DisplayText("This is a literal \
    string"); // // When a string is too long, use a backslash \ to continue the literal string on the next line. This does not indicate inserting a line break in the string. The above two ways of writing are completely equivalent.
    ```
    Literal strings support using backslash escape characters
    |Description|Explanation|Example|Result|
    |-|-|-|-|
    |\\\\ |Denotes \\ |`DisplayText("Hello\\SC");`|Hello\SC|
    |\octal|Denotes a octal ASCII code|`DisplayText("SC\101\102\103");`|SCABC|
    |\xhex|Denotes a hex ASCII code|`DisplayText("SC\x41\x42\x43");`|SCABC|
    |\\`newline`|Indicates continuing the line without a line break|`DisplayText("Hello\`<br />`SC");`|HelloSC|
    |\\n|Inserts a line break, equivalent to \x0A|`DisplayText("Hello\nSC");`|Hello<br />SC|
    |\\t|Inserts a tab, equivalent to \x09|`DisplayText("Hello\tSC");`|Hello&emsp;SC|
    |\\r|Inserts a return, equivalent to \x0D, no effect in the game|`DisplayText("Hello\rSC");`|HelloSC|
    |\\"|Denotes a double quote in a double quote string|`DisplayText("Hello\"SC\"");`|Hello"SC"|
    |\\'|Denotes a single quote in a single quote string|`DisplayText('Hello\'SC\'');`|Hello'SC'|


- ### Literal Bytes

    Literal bytes can be enclosed in `b"` to `"` or `b'` to `'`. Bytes will not end with `\0`. Literal bytes also support the escape characters in literal strings.  
    ```JavaScript
    println("{}", b"ASCII\nliteral");
    println("{}", b'ASCII\nliteral');
    ```


- ### Naming Rules

    Variable names, constant names and function names can only contain `non-ASCII UTF-8 characters` (Chinese, Japanese and Korean can be used),
    [ASCII](https://en.wikipedia.org/wiki/ASCII) letters/numbers and `_`, and cannot start with ASCII numbers.
    
    ```JavaScript
    // Legal variable names
    var a;
    var a_b;
    var a_1;
    var _a1;
    var 这也行;

    // Illegal variable names
    var 3y = 1;
    var abc# = 2;
    ```

    Variable names, constant names and function names cannot be named with keywords. I'm not sure which are keywords, but these are:  

    ```C#
    static var const object this function 
    return for foreach while switch epdswitch 
    break continue if else once import as 
    true false 
    ```

    Variable names and constant names cannot be named with Python 3 keywords:

    ```Python
    False None True 
    and as assert break class continue 
    def del elif else except finally 
    for from global if import in 
    is lambda nonlocal not or pass 
    raise return try while with yield 
    ```

    In addition, when a function name starts with `py_`, you have to call it with `py_py_` to call it.

    ```JavaScript
    function py_FuncName() {
    }
    function onPluginStart() {
        py_py_FuncName();
    }
    ```


- ### Importing Other Modules

    You can use the `import` keyword to import other modules. `as` gives an alias to the imported module. The following code illustrates the usage:  

    `Module1.eps`:
    ```JavaScript
    const A_CONST = 0; 
    static var A_VAR = 0;   

    function *A_FUNC*() {
        A_VAR++;
        return A_VAR;
    }
    ```

    `Module2.eps`:
    ```JavaScript
    import Module1;  

    function MODULE2_FUNC() {  
        return Module1.A_FUNC();  
    }
    ```

    `Module3.eps`:
    ```JavaScript
    import Module1 as m1; 
    import Module2 as m2;   

    function onPluginStart() {
        println("{}", m1.A_CONST);  
        m2.MODULE2_FUNC();  
    }
    ```


- ### Symbols

    All syntax-related symbols are half-width symbols in pure English state and can be found in the [ASCII](https://en.wikipedia.org/wiki/ASCII) table.  

    - #### Code Block

        Use curly braces `{}` to denote a code block in epScript.  

        ```JavaScript
        {
            // codes
        }
        ```

        If you want a single statement to be in a code block, you can omit the curly braces. The following example is valid:  

        ```JavaScript
        function ANNOYING_EXAMPLE_FUNC()
            for (var i = 1; i < 10; i++)
                if (i < 5)
                    println("{} < 5", i);
                else if (i == 5)
                    println("{} = 5", i);
                else
                    println("{} > 5", i);
        ```

    - #### Syntax Line Break

        The syntax line break is a semicolon `;` instead of a line break.

        ```JavaScript
        var a;var b;
        ```

    - #### Index Operator
        `[]`
        Used to access or modify elements in an array.  

        ```JavaScript
        const a = EUDArray(10);
        a[0] = 11;
        var b = a[0];
        ```

    - #### Assignment Operator

        The assignment operator is a single equal sign `=`  

        ```JavaScript
        var a; // Declare variable a  
        var b = 3; // Declare variable b and assign it to 3
        a = 2; // Assign variable a to 2 
        ```

    - #### Line Comment

        Two slashes `//` starts a line comment.

        ```JavaScript
        var a = 1; // Comments are parts of the code that will not be executed. // starts a comment that continues to the end of the current line.
        ```

    - #### Block Comment

        The content between `/*` to `*/` is a block comment.  

        ```JavaScript
        var /* This is a block comment, which can be placed in the middle of code */ a = 1;
        ```

    - #### Conditional Operator

        - Greater than `>`
        - Less than `<`
        - Greater than or equal to `>=`
        - Less than or equal to `<=`
        - Equal to `==`
        - Logical and `&&`
        - Logical or `||` 

        It is worth mentioning that when using conditional comparison operators on variables, what is returned is the `conditional expression` itself, not the `conditional expression result`.  
        The parameters of if are a list of `conditional expression`s. If a variable is passed directly to if, if will convert it into an expression that checks if its runtime value is not equal to 0.  

        ```JavaScript
        if (a == 2) // Double equals sign for logical equal 
            single_sentence;   

        if (a == 2) {
            // a is equal to 2
            single_sentence1; 
            single_sentence2; 
        }

        if (a != 2) { 
            // a is not equal to 2
        }

        if (a > 2) {  
            // a is greater than 2
        }

        if (a < 2) {    
            // a is less than 2 
        }

        if (a >= 2) {     
            // a is greater than or equal to 2
        }

        if (a <= 2) {      
            // a is less than or equal to 2  
        } 

        if (a > 2 && a < 10) {   
            // a is greater than 2 and less than 10
        }

        if (a > 10 || a <= 5) { 
            // a is greater than 10 or less than or equal to 5  
        }

        if ( ! (a < 2) ) {    
            // a is not less than 2
        }

        var a = 3;
        var b = a > 0;       // Error! It returns not true but the conditional expression a > 0 itself
        var c = l2v(a > 0);  // This is correct. At runtime, c will be equal to either true or false, depending on the runtime state of a.
        const d = a > 0;     // Here, d represents the conditional expression a > 0 itself, not the result of a > 0
        var e = l2v(d);      // At runtime, use l2v to assign the result of expression d to e
        ```

        - Logical not `!`  
        
        Using `!` on the variable `a` will return a variable whose value is the result of `l2v((a != 0) == 0)`.  
        Using double consecutive `!` on the variable `a`, such as `!!a` or `!(!a)` or `!!!(!a)` is directly equal to `a` itself.  
        Using `!` on a `constant` or a `conditional expression` will still return a `conditional expression`.  

        ```js
        var four = 4;
        var b = !four; // b == 0
        if (!b   != !!four) println("b is not !!four");
        if (four == !!four) println("four is !!four");
        ```

    - #### Mathematical Operators

        `+` `-` `*` `/`

        ```JavaScript
        a = a + 1;  
        a = a - 1;
        a = a * 2;
        a = a / 2;  // Integer division operator, rounding down  
        a = a % 2;  // Modulus operator   
        a = a ** 3; // This is the exponentiation operator, returns a to the power of 3
        a = a << 1; // Left bitwise shift by 1  
        a = a >> 1; // Right bitwise shift by 1
        ```

    - #### Increment/Decrement/Multiplication/Division Assignment Operators

        ```JavaScript
        a += 10; // Equivalent to a = a + 10;  
        a -= 10; // Equivalent to a = a - 10;  
        a++;     // Equivalent to a = a + 1;  
        a--;     // Equivalent to a = a - 1;
        a *= 10; // Equivalent to a = a * 10;
        a /= 10; // Equivalent to a = a / 10;
        ```


- ### Conditional Statement Syntax

    - #### if

        The syntax of if is  

        ```JavaScript
        if (conditional expression) {
            Execute when the conditional expression is true;
        }
        ```

    - #### if else

        The else branch of if  

        ```JavaScript
        if (conditional expression) {
            Execute when the conditional expression is true; 
        } else {
            Execute when the conditional expression is false;
        }
        ```

    - #### Conditional Chaining

        You can chain if to another else  

        ```JavaScript
        if (conditional expression 1) {
            Execute when conditional expression 1 is true;
        } else if (conditional expression 2) {
            Execute when conditional expression 1 is false and conditional expression 2 is true;
        } else {
            Execute when conditional expression 1 and conditional expression 2 are both false; 
        }
        ```

    - #### Conditional Nesting

        You can nest if within the code block of another if

        ```JavaScript
        if (conditional expression 1) {
            Execute when conditional expression 1 is true;
        } else if (conditional expression 2) {
            if (conditional expression 3) {
                Execute when conditional expression 1 is false, conditional expression 2 and conditional expression 3 are both true;
            } else {
                Execute when conditional expression 1 and conditional expression 3 are false, and conditional expression 2 is true; 
            }
        } else if (conditional expression 4) {
            Execute when conditional expression 1 and conditional expression 2 are false, and conditional expression 4 is true;
        } else {
            Execute when conditional expression 1 and conditional expression 2 are both false;
        } 
        ```

    - #### Once Execution

        As the name suggests, once execution will execute its internal code only once when the condition is met during runtime, and will not execute again. It is usually used to repeatedly determine in beforeTriggerExec or afterTriggerExec for each frame until the condition is met and executed once.  

        ```JavaScript
        once (condition expression) { // In a situation where the once code block is repeatedly running during runtime, it will only run the code inside it once when the conditional expression is satisfied. 
            // Codes
        }

        once { // Unconditionally execute the code inside it only once
            // Codes
        }

        // The following code will only print 0 once
        for (var i = 0; i < 100; i++) {
            once {
                println("{}", i);
            }
        }

        // The following code will only trigger once when any area/location between Location 1 to Location 10 has at least 1 Terran Marine, instead of triggering 10 times when entering each area/location separately. 
        for (var i = $L("Location 1"); i <= $L("Location 10"); i++) {
            once ( Bring(P1, AtLeast, 1, "Terran Marine", i) ) {
                println("Terran Marine has entered location {}", i);
            }
        }
        ```


- ### Control Flow

    - #### for Loop

        The for loop can set loop initialization expression, loop execution condition expression and loop additional action expression.  

        ```JavaScript
        for (initialization expression; loop execution condition expression; loop additional action expression) {
            Code in the loop;
        }

        for (var i = 0; i < 10; i++) {
            println("{}", i);
        }
        // Briefly, the above code declares a counter variable i, initially 0, and keeps looping as long as i < 10, incrementing i by 1 each time, and the scope of i is within the braces, which is the content that needs to be executed each time the loop iterates.

        var i1, i8;
        for (i1, i8 = 0, 0 ; i1 < 10 && i8 < 80 ; i1++, i8 += 8) {
            printAll("{} x 8 = {}", i1, i8);
        }
        ```

    - #### while Loop

        The while loop can set a loop condition, and will keep looping as long as the condition is satisfied, until the condition is not satisfied.

        ```JavaScript
        var i = 0;
        while (i < 10) {
            println("{}", i);
            i++;
        }
        ```

    - #### break

        You can use break to exit a running loop or switch statement.

        ```JavaScript
        var i = 0;
        while (true) { // Sets an always true condition, that is, always returns true
            println("{}", i);
            if (i >= 10) {
                break;
            }
        }
        ```

        It is equivalent to the while loop above.

    - #### foreach Iterator Loop

        **Compile-time Iterators**  
        py_range and py_enumerator are compile-time iterators.  
        Python containers (list, tuple, etc.) are compile-time iterators.  
        When using compile-time iterators, foreach is a compile-time loop that will be statically expanded at compile time and cannot use break and continue.  
        ```C#
        foreach (i : py_range(5)) {
            simpleprint(i + 1);
        }
        // Equivalent to the following code
        simpleprint(0 + 1);
        simpleprint(1 + 1);
        simpleprint(2 + 1);
        simpleprint(3 + 1);
        simpleprint(4 + 1);
        ```

        ```C#
        foreach (i : py_range(3)) {
            once (ElapsedTime(AtLeast, i)) {
                println("The {} secound(s)", i);
            }
        }
        // Equivalent to the following code
        once (ElapsedTime(AtLeast, 0)) {
            println("The {} secound(s)", 0);
        }
        once (ElapsedTime(AtLeast, 1)) {
            println("The {} secound(s)", 1);
        }
        once (ElapsedTime(AtLeast, 2)) {
            println("The {} secound(s)", 2);
        }
        ```

        ```C#
        const arrs = py_list();
        foreach (x : list(50, 100, 150)) {
            arrs.append(EUDArray(x));
        }
        // Equivalent to the following code
        const arrs = py_list();
        arrs[0] = EUDArray(50);
        arrs[1] = EUDArray(100);
        arrs[2] = EUDArray(150);
        ```

        **Runtime Iterators**  
        Iterator functions named EUDLoop* return runtime iterators.  

        > EUDLoopPlayer, EUDLoopRange, EUDLoopUnit, EUDLoopUnit2, EUDLoopCUnit, EUDLoopNewUnit, EUDLoopNewCUnit, EUDLoopPlayerUnit, EUDLoopPlayerCUnit  

        Secondly, EUDQueue, EUDDeque containers are also runtime iterators. UnitGroup.cploop also returns a runtime iterator.  

        EUDDeque example
        ```C#
        // dq3 is a size 3 EUDDeque
        const dq3 = EUDDeque(3)();
        const ret = EUDCreateVariables(6);

        // If dq3 is empty, no code will be executed at runtime
        foreach(v : dq3) {
            ret[0] += v;
        }

        // Add 1 and 2 to the right side of dq3 EUDDeque
        dq3.append(1);  // dq3 : (1)
        dq3.append(2);  // dq3 : (1, 2)
        foreach(v : dq3) {
            ret[1] += v; // 3 = 1 + 2
        }

        // Add 3 and 4 to the right side of dq3 EUDDeque
        dq3.append(3);  // dq3 : (1, 2, 3)
        dq3.append(4);  // dq3 : (2, 3, 4)
        foreach(v : dq3) {
            ret[2] += v; // 9 = 2 + 3 + 4
        }

        // Add 5 to the right side of dq3 EUDDeque
        dq3.append(5);  // dq3 : (3, 4, 5)
        foreach(v : dq3) {
            ret[3] += v; // 12 = 3 + 4 + 5
        }

        // Pop one value from the left side, here 3 is popped
        const three = dq3.popleft();  // dq3 : (4, 5)  
        foreach(v : dq3) {
            ret[4] += v; // 9 = 4 + 5
        }

        // Add 6 and 7 to the right side of dq3 EUDDeque
        dq3.append(6);  // dq3 : (4, 5, 6)
        dq3.append(7);  // dq3 : (5, 6, 7)
        foreach(v : dq3) {
            ret[5] += v; // 18 = 5 + 6 + 7
        }
        ```

    - #### switch

        Conditional branching for multiple states of a single runtime variable value.  

        **Normal Switch**
        ```JavaScript
        switch (day) {
            case 1: 
                DisplayText("The bitter working days begin");
                break;  
            case 4:
            case 5:
                DisplayText("The weekend is coming soon");
                break;   
            case 0, 6:
                DisplayText("So cool!");  
                break;
            default:
                DisplayText("Looking forward to the weekend");
        }

        // The above switch code can be viewed as the following if conditional branching code

        if (day == 1) {
            DisplayText("The bitter working days begin");
        } else if (day == 4 || day == 5) {
            DisplayText("The weekend is coming soon");  
        } else if (day == 0 || day == 6) { 
            DisplayText("So cool!");
        } else {
            DisplayText("Looking forward to the weekend");
        }
        ```

        **Switch with Bitmask**
        ```JavaScript
        var x = 0x101;
        switch (x, 0xff) {
            case 0:
                // (x & 0xff) == 0
                break;
            default:
                // (x & 0xff) != 0
                break;
        }
        ```

    - #### epdswitch

        Conditional branching for multiple states of a single runtime memory address value.

        ```JavaScript
        const unitId = epd + 0x64/4;
        epdswitch (unitId, 255) {  // you can put constant epd in epdswitch too
            // switch branching by unit kind
            case $U("Terran Marine"):
                // Run when unitType is marine
                break;
            case $U("Terran Ghost"):
                // Run when unitType is ghost
                break;
        }
        ```

      




---


# Use of Variables

<br />

- [Basic Description](#basic-description)
    - [Variable Declaration](#variable-declaration)
    - [Static Variables](#static-variables)
    - [Constant Declaration](#constant-declaration)
    - [Variable Assignment](#variable-assignment)
    - [Variable Scope](#variable-scope)
    - [Mathematical Operations Of Variables](#mathematical-operations-of-variables)
    - [Object Types](#object-types)
    - [Value Types, Reference Types](#value-types-reference-types)
    - [Runtime Strings](#runtime-strings)
    - [Appendix Static Or Dynamic Instantiation](#appendix-static-or-dynamic-instantiation)
    - [Explanation Of const And var](#explanation-of-const-and-var)

<br />

## Basic Description

All variables in epScript code allow desync modification or access. sync modification access belongs to synced-data, and desync modification access belongs to desync-data.  
epScript has only one value type variable, which is a 32-bit unsigned integer.  

- ### Variable Declaration

    You can use `var` syntax to declare a normal variable

    ```JavaScript
    var variableName1;
    static var variableName1 = 0;
    // The above two writings are equivalent
    var variableName2 = initialValue; 
    ```

- ### Static Variables

    In fact, all variables are implemented internally as static, but local variables are restored to their initial values each time.  
    Variables without an initial value have static properties. Using the `static` keyword to declare a variable can explicitly give it static properties.  

    ```JavaScript
    function increaseCount() {
        static var count = 5;
        return count++;
    }

    function onPluginStart() {
        println("{}", increaseCount()); // 6
        println("{}", increaseCount()); // 7
        println("{}", increaseCount()); // 8
    }
    ```


- ### Constant Declaration

    The value of a constant cannot be changed at runtime.  
    All reference types (objects) must be declared with the const modifier. The state of reference type objects can be changed at runtime, but the target object they refer to cannot be changed at runtime.  

    ```JavaScript
    const arrayVariableName1 = EUDArray(arraySize);
    const object1 = objectTypeName();
    ```


- ### Variable Assignment

    The value of a variable can be changed at runtime. After declaration, the equal sign (`=`) can be used to assign a value to the variable.

    ```JavaScript
    var variableName1; // Declare variable

    variableName1 = 100; // Assign variable to 100
    variableName1 = variableName1 + 2;  // Increment variable by 2
    ```


- ### Variable Scope

    The scope of a variable is from its declaration down to leaving the current layer of braces (or file). Variables of the same name in inner scopes have higher priority than those in outer scopes.   
    Although unnecessary, here is an incorrect example:  
    ```JavaScript
    var moduleLevelVariable = 100;

    function incorrectExample() {
        localVariable1 = 2; // This is wrong because localVariable1 is declared in the next line 
        var localVariable1 = 2; 
        {
            localVariable1 = 1;
            var localVariable2 = 2;
            var localVariable1 = 100; 
            localVariable2 = localVariable1; // There are two localVariable1, take the one with the smaller and more specific scope, which is 100
            localVariable2 = moduleLevelVariable;
        }
        localVariable1 = localVariable2; // This is wrong because localVariable2 is declared inside that layer of braces, it can not leave its scope
        localVariable1 = moduleLevelVariable;
    }
    ```


- ### Mathematical Operations Of Variables

    Although variables can only be 32-bit unsigned integers, variables can represent negative numbers, like unsigned 32-bit integers in C language.  
    ```JavaScript
    var a = 0;
    a -= 2;
    if (a > 0) { // This condition is true, the negative number of an unsigned number is greater than the positive number
        println("a == 0x{:x}", a); // a == 0xFFFFFFFE
    }
    if (a >= 0x80000000) { // To determine if a is negative, it should be judged like this
        println("a(-{}) is less than 0", -a); // a(-2) is less than 0
    }
    if (a < -1 && a > -3) { // This is true
        println("a(0x{:x}) is less than -1 and greater than -3", a); // a(0xFFFFFFFE) is less than -1 and greater than -3
    }
    a -= 1; 
    if (a == -3) { // This is true
        println("a(0x{:x}) is now equal to -3", a); // a(0xFFFFFFFD) is now equal to -3
    }
    var b = 0;
    DoActions(b.SubtractNumber(2)); // This is invalid, Subtract action cannot subtract the value below 0
    println("b == 0x{:x}", b); // b == 0x00000000
    ```


- ### Object Types

    Object types are reference types, which are different from value types.

    ```JavaScript
    object ObjectTypeName {
        var fieldName1; 
        var fieldName2;
        var fieldName3;
        function methodName1_AssignValueToField1(value) { 
            this.fieldName1 = value;
        }
        function GetTheValueOfField1() {
            return this.fieldName1;
        }
    };
    ```

    - #### There are two ways to create an object instance  

        - Static initialization: `const object1 = ObjectTypeName();`  
        - Dynamic initialization: `const object1 = ObjectTypeName.alloc();` You can pass it to any scope for use. Remember to release the memory it occupies with `ObjectTypeName.free(object1);`  


- ### Value Types, Reference Types

    Value types

    ```JavaScript
    var a = 27;
    var b = a;
    b = 3;
    println("{}, {}", a, b); // Outputs 27, 3
    ```

    Reference types

    ```Java
    const a = EUDArray(1);
    a[0] = 27;
    const b = a;
    b[0] = 3;
    println("{}, {}", a[0], b[0]); // Outputs 3, 3
    ```

    Reference types pass the memory address of the value, while value types pass the value itself.


- ### Runtime Strings

    You can use GetMapStringAddr to get the address of the map string in memory and use memory functions to modify its content (unable to change the string size).  

    ```JavaScript
    const buf_index = GetStringIndex(py_str(" ") * 64); // A string of length 64, all spaces
    const buf_addr = GetMapStringAddr(buf_index);
    dbstr_print(buf_addr, "String 1"); 
    DisplayText(buf_index);
    dbstr_print(buf_addr, "String ", 2); 
    DisplayText(buf_index);
    ```

    Implement using StringBuffer to operate memory buffers (unable to change string size).  

    ```JavaScript
    const buf = StringBuffer(64);
    buf.insertf(0, "String {}", 1);
    buf.append("String 2");
    buf.DisplayAt(6); // Output display to line 6 of the screen text
    DisplayText(buf.StringIndex);
    ```

    Use Db memory data (unable to change string size).  

    ```JavaScript
    const buf_addr = Db(64);
    dbstr_print(buf_addr, "String 1");
    simpleprint(buf_addr);
    dbstr_print(buf_addr, "String ", 2);
    simpleprint(buf_addr);
    ```


- ### Appendix Static Or Dynamic Instantiation

    Every variable in epScript has fixed memory address. So every variable is persistent. For example, consider this code.

    ```JavaScript
    function x() {
        var y;
        y++;
        return y;
    }
    ```

    It is roughly equivalent to the following code (the difference is that the scope of y in the above code is inside the x function, while the scope of x__y in the following code is the entire module containing the x function):  

    ```JavaScript
    var x__y;

    function x() {
        x__y++;
        return x__y;
    }
    ```

    The results are:

    ```JavaScript
    var a = x();  // returns 1
    var b = x();  // returns 2
    var c = x();  // returns 3
    ```

    > **warning**
    > A local variable only has static properties when you do not initialize it. If you declare a variable with var y = 0; and initialize it, the value of y will be 0 every time x is called. euddraft's behavior for initializing and not initializing variables may lead to confusion. You should not rely on this feature to write code, it is best to explicitly specify initial values for all variables. If you want a variable to have static properties, you can explicitly declare it with the static keyword and explicitly specify an initial value, even if it is 0.  

    Same applies for objects. All objects, local, global, or temporary, have fixed memory space. Consider this code for example.

    ```JavaScript
    function main() {
        const X = EUDArray(10);
        for (var i = 0 ; i < 10 ; i++) {
            X[i] = EUDArray(10);
        }
    }
    ```

    You may think that we're assigning a separate `EUDArray(10)` instance for each cell of X, but this code don't act like that.The code above is equivalent to:

    ```JavaScript
    const _t0 = EUDArray(10);  // Even intermediate values are static
    const _t1 = EUDArray(10);  // Even intermediate values are static

    function main() {
        const X = _t0;
        for (var i = 0 ; i < 10 ; i++) {
            X[i] = _t1;
        }
    }
    ```

    This is not what you might expect. All cells of X points to the same `_t1` EUDArray.  
    We need to use dynamic instantiation like `X[i] = EUDArray.alloc(10);` to assign 10 different EUDArray to each X cell. Sadly EUDArray cannot be dynamically instantiated, so it doesn't have `.alloc()`. So we cannot fix this code.  

    Although we cannot dynamically create arrays at runtime, we can still statically allocate buffers and dynamically use them at runtime. Refer to the following code:  

    ```JavaScript
    function onPluginStart() {
        const X = EUDArray(10);
        foreach (i : py_range(5)) {
            X[i] = EUDArray(10);
        }
        const X_2 = EUDArray.cast(X[2]);
        X_2[3] = 4;
        println("{}", X_2[3]);
    }
    ```

    The above code is equivalent to:  

    ```JavaScript
    function onPluginStart() {
        const X = EUDArray(10);
        X[0] = EUDArray(10);
        X[1] = EUDArray(10);
        X[2] = EUDArray(10);
        X[3] = EUDArray(10);
        X[4] = EUDArray(10);
        const X_2 = EUDArray.cast(X[2]);
        X_2[3] = 4;
        println("{}", X_2[3]);
    }
    ```

    Reference: [https://github.com/phu54321/euddraft/wiki/9B.-Appendix---Static-or-Dynamic-instantiation](https://github.com/phu54321/euddraft/wiki/9B.-Appendix---Static-or-Dynamic-instantiation)



- ### Explanation Of const And var
    The essence of const is to declare a variable at the Python (compile time), not a map runtime variable. When declaring an object, it stores the runtime address of the referenced object.  
    The essence of var is syntactic sugar for declaring a reference to an EUDVariable object, which is a map runtime variable.  
    The difference from const is that at compile time, it will compile the assignment operation `=` into the left shift operator `<<` at the Python. The left shift operator of runtime types is usually overloaded to change the value stored in the runtime object, while the const at the syntax level does not allow the use of the assignment operator `=` after declaring the initial value.  

    If you use var to declare an EUDArray, the essence is to declare an EUDVariable that stores the address of an EUDArray object. Using index operations on this variable will throw an syntax error because it is an EUDVariable rather than an EUDArray.  

    ```JavaScript
    var arr = EUDArray(10);
    arr[0] = 1; // Syntax error! arr is an EUDVariable and does not support index operators. It internally stores the address of an EUDArray object.
    const arrt = EUDArray.cast(arr); // You can do this to wrap the value of arr into an EUDArray object  
    arrt[0] = 1;
    ```

    The following illustrates the relationship between var and const. The two pieces of code are equivalent.

    ```JavaScript
    var variableName = 3;
    variableName = 4;
    variableName += 5;
    println("{}", variableName);
    ```

    ```JavaScript
    const variableName = EUDVariable(3);
    variableName.__lshift__(4);
    variableName.__iadd__(5);
    println("{}", variableName);
    ```

    Compile-time interaction that can be done in epScript

    ```JavaScript
    var v = 100;
    const i = 10;
    const s = py_str("Location ") + py_str(i);
    py_print(py_str("Compiled to const s = {}").format(s));
    py_print("v is a ", v, " object");
    ```

      




---


# Use of Functions

<br />

- [Functions](#functions)
    - [Declarations](#function-declarations)
    - [Implementation](#function-implementation)
    - [Parameters](#function-parameters)
    - [Return Values](#function-return-values)
    - [Parameter And Return Value Types](#parameter-and-return-value-types)
    - [Calls](#function-calls)
    - [Explanation Of Multiple Return Values](#explanation-of-multiple-return-values)

<br />

## Functions

- ### Function Declarations

    ```JavaScript
    function aFunction();
    ```

    If a function is not declared, it will be declared at the location where it is implemented.


- ### Function Implementation

    ```JavaScript
    function aFunction() {
        // Codes
    }
    ```


- ### Function Parameters

    A function can have one or more parameters, separated by commas. Parameter passing and return value passing are done through runtime value type variables (EUDVariable).

    ```JavaScript
    function printTwoVariableValues(parameter1, parameter2) {
        println("{}, {}", parameter1, parameter2);
    }
    ```


- ### Function Return Values

    A function can return one or more values after being called, with multiple return values separated by commas.

    ```JavaScript
    function exchange(value1, value2) {
        return value2, value1;
    }
    ```


- ### Parameter And Return Value Types
    Function parameters and return values can set types.  
    To set the parameter type, add a colon after the parameter name and write the type name, indicating that the runtime parameter value (as a number or pointer) will be set to the specified type.   
    To set the return value type, add a colon after the closing parenthesis of the function declaration parameter list and write the type name, indicating that the returned runtime value (as a number or pointer) will be set to the specified type.  

    ```JavaScript
    function createANewUnit(player : TrgPlayer, ut : TrgUnit, loc : TrgLocation) : CUnit, TrgString {
        const cu = CUnit.from_read(EPD(0x628438));
        if (cu == 0) {
            return 0, $T("Unable to create unit");  
        }
        CreateUnit(1, ut, loc, player);
        if ( Memory(0x628438, Exactly, cu.ptr) ) {  
            return 0, $T("CreateUnit failed to create the unit, possibly incorrect parameters or the location can no longer place more units.");
        }
        return cu, $T("Success");
    }

    function onPluginStart() {
        const cu, err = createANewUnit(P1, $U("Terran Marine"), $L("Location 1"));
        if (cu != 0) {
            cu.cgive(P8);
            cu.set_color(P8);
        } else {
            DisplayTextAll(err);
        }
    }
    ```

- ### Function Calls

    ```JavaScript
    aFunction(); // Directly call a function without arguments

    var a = 2;  
    var b = 3;

    a, b = exchange(a, b); // Pass arguments to call a function and get its return value

    printTwoVariableValues(a, b); // Pass arguments to call a function   
    ```

- ### Explanation Of Multiple Return Values
    A function that returns multiple return values actually returns a compile-time tuple. When you do not need to get all the return values, you can use selection `[[]]` to get one or more (starting from index 0) from the returned tuple.  
    A tuple is a compile-time type, not a runtime data structure.  

    ```JavaScript
    function aFunctionWithMultipleReturnValues() {
        return 1, 2, 3, 4, 5;  
    }

    const r1 = aFunctionWithMultipleReturnValues()[[0]];

    const r4, r3 = aFunctionWithMultipleReturnValues()[[4, 3]];

    const r1, r2, r3, r4, r5 = aFunctionWithMultipleReturnValues(); // When there are enough left values to receive multiple return values, the tuple will automatically unpack
    ```

---


# Use of Objects

<br />

- [Object types](#object-types)
    - [Declarations](#declarations)
    - [Creating Instances](#creating-instances)

<br />

## Object types
Object types are reference types.

- ### Declarations

    You can only declare object in module scope, and must put semicolon at end of definition.

    You can declare an object type as follows:  

    ```JavaScript
    object ObjectTypeName { 
        var fieldName1; 
        var fieldName2;
        var fieldName3;
        function methodName1_assignValueToField1(value){
            this.fieldName1 = value;
        }
        function getTheValueOfField1() { 
            return this.fieldName1;
        }
    };
    ```

    You can define constructor and destructor:

    ```js
    const objList = EUDArray(100);
    var objCount = 0;
    object Obj {
        var a, b, c;
        var index;
        function constructor(a, b, c) {
            this.a = a;
            this.b = b;
            this.c = c;

            this.index = objCount;
            objList[objCount] = this;
            objCount++;
        }
        function destructor() {  // runs on Obj.free(instance)
            objCount--;
            const lastObj = objList[objCount];
            objList[this.index] = lastObj;
        }
    };

    const staticObj = Obj(1, 2, 3);
    const dynObj = Obj.alloc(1, 2, 3);
    ```

    `(there's constructor_static but defining it in epScript has limitation.)`

    The following declares a Date object type

    ```JavaScript
    object Date {
        var year, month, day, hour, minute, second;
        /***
         * weekday: {0 = Sunday, 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday}
         * @type {number}
         * @public
         */
        var weekday;

        function update_timestamp(unixTimestamp) {
            const MONTH_DAYS = EUDArray(list(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31));
            var year, month, day = 1970, 1, 1;
            var days, seconds = div(unixTimestamp, 86400);
            const weekday = (days + 4) % 7;

            while (true) {
                for (var m = 0 ; m < 12 ; m++) {
                    var daysInMonth = maskread_epd(EPD(MONTH_DAYS) + m, 31);
                    // January of leap year (year is multiple of 4)
                    if (m == 0 && year.ExactlyX(0, 3)) daysInMonth += 1;
                    if (days < daysInMonth) {
                        day = days + 1;
                        days = 0;
                        break;
                    }
                    days -= daysInMonth;
                    month += 1;
                }
                EUDSetContinuePoint();
                if (days == 0) break;
                month = 1;
                year += 1;
            }
            const hour, minuteAndSecond = div(seconds, 3600);
            const minute, second = div(minuteAndSecond, 60);

            this.year = year;
            this.month = month;
            this.day = day;
            this.hour = hour;
            this.minute = minute;
            this.second = second;
            this.weekday = weekday;
        }
    };
    ```


- ### Creating Instances
    - There are two ways to create an object instance:  
        - Static initialization: `const object1 = ObjectTypeName()`;  
        - Dynamic initialization: `const object1 = ObjectTypeName.alloc();` You can pass it to any scope for use. Remember to use `ObjectTypeName.free(object1);` to free the memory it occupies when done.  

    The following is an example of using the Date object instance:  
    ```JavaScript
    function afterTriggerExec() {

        var timestamp;
        var previousSysTime;
        const newSysTime = dwread(0x51CE8C);
        once {
            timestamp = dwread(0x6D0F38);  // game start timestamp
            previousSysTime = newSysTime;
        }
        static var cumulativeSysTime = 0;
        cumulativeSysTime += (previousSysTime - newSysTime);  // time difference
        previousSysTime = newSysTime;

        const date = Date();

        if (cumulativeSysTime >= 1000) {
            const second, millisecond = div(cumulativeSysTime, 1000);
            cumulativeSysTime = millisecond;
            timestamp += second;
            // date.update_timestamp(timestamp);
            date.update_timestamp(8 * 3600 + timestamp);
        }

        const weekdayToName = function (weekday) {
            switch (weekday) {
                case 0: return EPD(Db("Sun"));
                case 1: return EPD(Db("Mon")); 
                case 2: return EPD(Db("Tue"));
                case 3: return EPD(Db("Wed"));
                case 4: return EPD(Db("Thu"));
                case 5: return EPD(Db("Fri"));  
                case 6: return EPD(Db("Sat"));
            }
        };

        printAllAt(10, "\x13\x04CST : {}-{}-{}({:t} ) {}:{}:{}",
            date.year, date.month, date.day, weekdayToName(date.weekday), date.hour, date.minute, date.second);

    }
    ```




---


# Understanding Strings

<br />

- Strings
    - [Compile-time Strings](#compile-time-strings-py_str)
    - [Map Strings](#map-strings-trgstring)
    - [String Data](#string-data-db)
    - [TBL Strings](#tbl-strings-stat_txttbl)

<br />

- ## Compile-time Strings (py_str)

    Compile-time strings refer to strings generated at compile time that will never be inserted into the map. They contain all literal strings and compile-time string constants.   
    Because the epScript compiler is implemented in Python, it is called py_str. Compile-time strings cannot be used directly for map runtime.  

    <details>
    
    <summary>When a function parameter is one of the following types, epScript will convert the incoming compile-time string argument into the corresponding constant number</summary>

    - [TrgUnit](Constants-Reference/TrgUnit.md)  
    - [TrgLocation](Constants-Reference/Constants-Reference.md#trglocation)  
    - [TrgSwitch](Constants-Reference/Constants-Reference.md#trgswitch)  
    - [TrgAIScript](Constants-Reference/TrgAIScript.md)  
    - [Weapon](Constants-Reference/Weapon.md)  
    - [Tech](Constants-Reference/Tech.md)  
    - [Upgrade](Constants-Reference/Upgrade.md)  
    - [UnitOrder](Constants-Reference/UnitOrder.md)  
    - [Flingy](Constants-Reference/Flingy.md)  
    - [Image](Constants-Reference/Image.md)  
    - [Icon](Constants-Reference/Icon.md)  
    - [Iscript](Constants-Reference/Iscript.md)  
    - [Portrait](Constants-Reference/Portrait.md)  
    - [Sprites](Constants-Reference/Sprites.md)  
    - [StatText](Constants-Reference/StatText.md)  
    </details>

    Here is an example to illustrate:

    ```JavaScript
    SetDeaths(P1, Add, 10, "Terran Marine"); // The corresponding parameter type of the SetDeaths action is TrgUnit, so it will be replaced with the integer ID in the TrgUnit table at compile time 
    ```

    The string "Terran Marine" in the above code will not be inserted into the map. 

    "Terran Marine" is only used at compile time to query the ID of the unit type (the ID of the Marine is 0).

    If human readability is not considered, the above code is completely equivalent to the following code:

    ```JavaScript
    SetDeaths(P1, Add, 10, 0);
    ```

    In epScript, you can also use py_str to declare a compile-time string constant.

    ```JavaScript
    const csTerran_  = py_str("Terran ");
    const csMarine   = py_str("Marine");
    const csGoliath  = py_str("Goliath");
    py_print(csMarine, " ", csGoliath); // Output Marine Goliath in the compile-time CLI
    SetDeaths(P1, Add, 10, csTerran_ + csGoliath);
    ```

     At compile time, you can get the ID of the compile-time string in different constant tables through the macro index.

    ```JavaScript
    const utTerranMarine = $U("Terran Marine");
    const stTerranMarine = $B("Terran Marine");
    py_print(utTerranMarine, stTerranMarine); // Output 0 1 in the compile-time CLI
    if (utTerranMarine == stTerranMarine) {   // This is equivalent to if (0 == 1) {
        simpleprint("So this message is never printed");
    }
    ```

    You can use the EncodeString macro to insert a compile-time string into the map as a map string (TrgString) and return its ID in the map string table.

    ```JavaScript
    const csTerran_  = py_str("Terran ");
    const csMarine   = py_str("Marine");
    const csTerran_Marine  = csTerran_ + csMarine;
    const str_idx = EncodeString(csTerran_Marine * 3);
    DisplayText(str_idx); // Output: Terran MarineTerran MarineTerran Marine
    ```



- ## Map Strings (TrgString)

    <details>
    
    <summary>Related types and functions</summary>

    - TrgString
    - StringBuffer
    - $T(cstr : [literal](Syntax.md#literal-strings))
    - EncodeString(cstr: py_str)
    - GetStringIndex(cstr: py_str)
    - GetMapStringAddr(str: TrgString)
    </details>
    
    Map strings (TrgString) are the most commonly used runtime strings.  
    When we use any custom string in the map editor, the map editor will insert this string into the map string table in the map file and assign it an ID.   
    For example, if we set the Map Title to "An interesting StarCraft map", this map title is a map string (TrgString) and is usually assigned the ID 1.  
    The string parameters of trigger action functions are this ID.  

    ```JavaScript
    DisplayText(1);          // Output: An interesting StarCraft map 
    SetMissionObjectives(1); // Mission objectives: An interesting StarCraft map
    ```

    In epScript code, if a compile-time string is passed as an argument where the function parameter type is TrgString, this string will first be inserted into the map string table of the map, and then its ID will be passed to that argument position.

    ```JavaScript
    DisplayText("Hello StarCraft");
    ```

    The above code is actually equivalent to:

    ```JavaScript
    const str_idx = EncodeString("Hello StarCraft");
    DisplayText(str_idx);
    ```

    You can also write it using $T syntax:

    ```JavaScript
    const str_idx = $T("Hello StarCraft");
    DisplayText(str_idx);
    ```

    Here is an example of a custom function that accepts map string parameters:

    ```JavaScript
    function test(strId : TrgString) {
        println("String ID:{}", strId);
        DisplayText(strId);
    }

    function onPluginStart() {
        test("Hello StarCraft");
        // Outputs:
        // String ID:3 
        // Hello StarCraft
    }
    ```

    You can also construct a very long compile-time empty string using the EncodeString macro to convert it into a map string (TrgString) to act as a string buffer like a string variable.

    ```JavaScript
    const buf_idx = EncodeString(py_str(" ") * 128);
    const buf_addr = GetMapStringAddr(buf_idx);
    for (var i = 1; i < 10; i++) {
        dbstr_print(buf_addr, "Line text ", i);
        DisplayText(buf_idx);
    }
    ```

    Of course, we do not need to build and maintain map strings (TrgString) ourselves as string buffers. Using the StringBuffer object can more easily dynamically manage a map string (TrgString) of a specific length.

    ```JavaScript
    const buf = StringBuffer(127);
    for (var i = 1; i < 10; i++) {
        buf.insert(0, "Line text ", i);
        buf.Display(); // DisplayText(buf.StringIndex);
    }
    ```

    More conveniently, epScript provides a series of print functions so that outputting text to the screen does not require maintaining StringBuffer yourself. 

    epScript maintains a GlobalStringBuffer with a capacity of 1023 bytes to implement the print function series. That is to say, strings less than this length can be output directly using the print function series.

    ```JavaScript
    for (var i = 1; i < 10; i++) {
        simpleprint("Line text ", i);
    }
    ```



- ## String Data (Db)
    <details>
    
    <summary>Related types and functions</summary>

    - Db  
    - dbstr_addstr(dst, src)  
    - dbstr_addstr_epd(dst, srcepd)  
    - dbstr_adddw(dst, number)  
    - dbstr_addptr(dst, ptr)  
    - dbstr_print(dst, *args)  
    - sprintf(dst, format_string, *args)  
    </details>

    Db strings are also a kind of runtime custom string.  
    However, unlike map strings (TrgString), they do not have an ID, so they cannot be directly applied to classical trigger actions.  
    Usually, some runtime string components need to be stored using Db. They do not necessarily each have an ID.  
    They can be copied to StringBuffer or other TrgStrings to pass to classical trigger actions.  

    ```JavaScript
    const buf = Db(128);
    const str = StringBuffer(1024);
    str.insert(0);
    for (var i = 1; i < 10; i++) {
        dbstr_print(buf, "Mission objective: Line text ", i);
        if (i < 9)
            str.append(buf, "\n");
        else
            str.append(buf);
    }
    str.Display();
    SetMissionObjectives(str.StringIndex);
    ```



- ## TBL Strings (stat_txt.tbl)
    <details>
    
    <summary>Related types and functions</summary>
    
    - $B([TBLKey](Constants-Reference/StatText.md) : [literal](Syntax.md#literal-strings))
    - EncodeTBL([TBLKey](Constants-Reference/StatText.md) : py_str)
    - GetTBLAddr([TBLKey](Constants-Reference/StatText.md))
    - settbl([TBLKey](Constants-Reference/StatText.md), offset, *args)
    - settbl2([TBLKey](Constants-Reference/StatText.md), offset, *args)
    </details>

    TBL strings refer to strings in Starcraft's internal string table, containing unit names, tech names, ability names, etc.   
    You cannot add strings to the TBL string table. You can find the ID corresponding to all TBLKeys from [StatText](Constants-Reference/StatText.md).  
    The string in memory corresponding to the TBLKey is not equal to the TBLKey itself.  

    ```JavaScript
    println("{:s}", GetTBLAddr("Terran Siege Tank (Tank Mode)")); // Output: Terran Siege Tank
    ```

    You can modify the names of units and abilities by modifying strings in the TBL table.s

    ```JavaScript
    dbstr_print(GetTBLAddr("Terran Marine"), "机枪兵\x00"); // Modifying tbl will cause localization to fail. All unit and ability names that have not been modified will become English. Strongly not recommended to modify tbl.
    ```

    

  




---


# Built-in Basic Object Types

<br />

- [Basic Object Types](#basic-object-types)
    - [EUDVariable](#eudvariable)
    - [EUDLightVariable](#eudlightvariable)
    - [EUDLightBool](#eudlightbool)
    - [EUDArray](#eudarray)
    - [EUDVArray](#eudvarray)
    - [PVariable](#pvariable)
    - [EUDVArrayReader](#eudvarrayreader)
    - [EUDDeque](#euddeque)
    - [StringBuffer](#stringbuffer)
        - [StringBuffer](#stringbuffer)
        - [.insert](#insert)
        - [.append](#append)
        - [.delete](#delete)
        - [.Display](#display)
        - [.print](#print)
        - [.Play](#play)
        - [.fade](#fade)
    - [Db](#db)
    - [EUDByteStream](#eudbytestream)
    - [~~CPString~~](#cpstring)
    - [~~DBString~~](#dbstring)

<br />

## Basic Object Types

- ### EUDVariable

    It is actually the variable declared with var. It is also an object, but it is syntactically defined as a value type, so it has some differences from other object types, such as being assignable with =, etc.  
    An EUDVariable will use a virtual trigger with only one SetDeathsX action to simulate, occupying 72 bytes. Here is its type structure. It has many conditional and action functions.  
    ```JavaScript
    object EUDVariable {
        // Common methods
        function ineg(){}                // Added in euddraft 0.9.9.8, Negate variable in-place (same as x = -x;). Supports action alternative DoActions(v.ineg(action = true));
        function iabs(){}                // Added in euddraft 0.9.9.8, Self-assign absolute value in-place (same as x = (x & (1 << 31) == 0) ? x : -x;). Supports action alternative DoActions(v.iabs(action = true));

        // Common conditions
        function AtLeast(v){}               // Variable value >= v
        function AtMost(v){}                // Variable value <= v 
        function Exactly(v){}               // Variable value == v
        function AtLeastX(v,mask){}         // Variable (value & mask) >= v
        function AtMostX(v,mask){}          // Variable (value & mask) <= v
        function ExactlyX(v,mask){}         // Variable (value & mask) == v
        function MaskAtLeast(v){}           // The Mask of the SetDeathsX action of the variable's virtual trigger >= v
        function MaskAtMost(v){}            // The Mask of the SetDeathsX action of the variable's virtual trigger <= v
        function MaskExactly(v){}           // The Mask of the SetDeathsX action of the variable's virtual trigger == v
        function MaskAtLeastX(v,msk){}      // (The Mask of the SetDeathsX action of the variable's virtual trigger & msk) >= v
        function MaskAtMostX(v,msk){}       // (The Mask of the SetDeathsX action of the variable's virtual trigger & msk) <= v 
        function MaskExactlyX(v,msk){}      // (The Mask of the SetDeathsX action of the variable's virtual trigger & msk) == v

        // Common actions
        function SetNumber(v){}             // Variable value = v
        function AddNumber(v){}             // Variable value = value + v
        function SubtractNumber(v){}        // Variable value = value - v if value <= v else value = 0
        function SetNumberX(v,mask){}       // Variable value = value - (value & mask) + (v & mask)
        function AddNumberX(v,mask){}       // Variable value = value - (value & mask) + ( ((value & mask) + (v & mask)) & mask )  
        function SubtractNumberX(v,mask){}  // Variable value = value - (value & mask) + ( ((value & mask) - (v & mask)) & mask )
    
        // Compile-time constant functions
        function GetVTable(){}              // Get the runtime address of the variable's virtual trigger at compile time
        function getMaskAddr(){}            // Get the runtime address of the Mask parameter in the SetDeathsX action of the variable's virtual trigger at compile time
        function getValueAddr(){}           // Get the runtime address of the value parameter in the SetDeathsX action of the variable's virtual trigger at compile time 
        function getDestAddr(){}            // Get the runtime address of the PlayerID parameter in the SetDeathsX action of the variable's virtual trigger at compile time

        // These methods of EUDVariable are practically only usable in combination with VProc
        function SetMask(v){}               // Set the Mask of the SetDeathsX action of the variable's virtual trigger to v
        function AddMask(v){}               // Set the Mask of the SetDeathsX action of the variable's virtual trigger to Mask + v
        function SubtractMask(v){}          // Set the Mask of the SetDeathsX action of the variable's virtual trigger to Mask - v if Mask >= v else Mask = 0  
        function SetMaskX(v,msk){}          // Set the Mask of the SetDeathsX action of the variable's virtual trigger to Mask - (Mask & msk) + (v & msk)
        function AddMaskX(v,msk){}          // Set the Mask of the SetDeathsX action of the variable's virtual trigger to Mask - (Mask & msk) + ( ((Mask & msk) + (v & msk)) & msk ) 
        function SubtractMaskX(v,msk){}     // Set the Mask of the SetDeathsX action of the variable's virtual trigger to Mask - (Mask & msk) + ( ((Mask & msk) - (v & msk)) & msk )
        function SetDest(dest){}            // Set the PlayerID of the SetDeathsX action of the variable's virtual trigger to dest
        function AddDest(dest){}            // Set the PlayerID of the SetDeathsX action of the variable's virtual trigger to PlayerID + dest
        function SubtractDest(dest){}       // Set the PlayerID of the SetDeathsX action of the variable's virtual trigger to PlayerID - dest if PlayerID >= dest else PlayerID = 0
        function SetDestX(dest,mask){}      // Set the PlayerID of the SetDeathsX action of the variable's virtual trigger to PlayerID - (PlayerID & mask) + (dest & mask)
        function AddDestX(dest,mask){}      // Set the PlayerID of the SetDeathsX action of the variable's virtual trigger to PlayerID - (PlayerID & mask) + ( ((PlayerID & mask) + (dest & mask)) & mask )
        function SubtractDestX(dest,mask){} // Set the PlayerID of the SetDeathsX action of the variable's virtual trigger to PlayerID - (PlayerID & mask) + ( ((PlayerID & mask) - (dest & mask)) & mask )
        function SetModifier(modifier){}    // Set the value modification method of the SetDeathsX action of the variable's virtual trigger to modifier
        function QueueAssignTo(dest){}      // Set the PlayerID of the SetDeathsX action of the variable's virtual trigger to dest and set the value modification method to SetTo
        function QueueAddTo(dest){}         // Set the PlayerID of the SetDeathsX action of the variable's virtual trigger to dest and set the value modification method to Add      
        function QueueSubtractTo(dest){}    // Set the PlayerID of the SetDeathsX action of the variable's virtual trigger to dest and set the value modification method to Subtract. The Subtract method cannot subtract a value from positive to negative.
    };
    ```

<br />

- ### EUDLightVariable

    Light variables are different from variables declared with var. They only occupy 4 bytes of memory space. Their value passing operations consume more resources than ordinary variables. Comparing values or writing values is the same as ordinary variables and only requires executing one trigger.  
    To pass its value as an argument to other functions, you need to use the dwread function to read it.  
    If the value of an ordinary variable (EUDVariable) does not need to be passed as an argument to other functions (for example, used for counting comparisons, incrementing, decrementing, assigning, switching, etc. scenarios not associated with other functions/conditions/actions), EUDLightVariable can be used instead of the ordinary variable.  


    ```JavaScript
    object EUDLightVariable {
        // Compile-time constant functions
        function getValueAddr(){}        

        // The goals that can be achieved by the following functions, conditions and actions can optionally use EUDLightVariable, otherwise an ordinary variable (EUDVariable) should be used.
        // Common methods
        function ineg(){}                   // Negate variable in-place (same as x = -x;). Supports action alternative DoActions(v.ineg(action = true)); in euddraft 0.9.9.8 and later versions
        function iabs(){}                   // Added in euddraft 0.9.9.8, Self-assign absolute value in-place (same as x = (x & (1 << 31) == 0) ? x : -x;). Supports action alternative DoActions(v.iabs(action = true));
        // Common conditions
        function AtLeast(v){}               // Light variable value >= v
        function AtMost(v){}                // Light variable value <= v 
        function Exactly(v){}               // Light variable value == v
        function AtLeastX(v,mask){}         // (Light variable value & mask) >= v
        function AtMostX(v,mask){}          // (Light variable value & mask) <= v 
        function ExactlyX(v,mask){}         // (Light variable value & mask) == v
        // Common actions
        function SetNumber(v){}             // Light variable value = v
        function AddNumber(v){}             // Light variable value = value + v
        function SubtractNumber(v){}        // Light variable value = value - v if value <= v else value = 0
        function SetNumberX(v,mask){}       // Light variable value = value - (value & mask) + (v & mask)
        function AddNumberX(v,mask){}       // Light variable value = value - (value & mask) + ( ((value & mask) + (v & mask)) & mask )  
        function SubtractNumberX(v,mask){}  // Light variable value = value - (value & mask) + ( ((value & mask) - (v & mask)) & mask )
    };
    ```

    Example

    ```JavaScript
    const lv = EUDLightVariable(100);
    DoActions(lv.AddNumber(564)); // lv += 564;
    if (lv != 150) {
        println("{}", dwread(lv.getValueAddr())); // This process of reading the value consumes more triggers than ordinary variables, about 32 times or more
    } 
    lv.ineg(); // lv = -lv;
    if (lv > 0x80000000 && lv < -663) {
        println("Less than -663 negative number");
    }
    ```

<br />

- ### EUDLightBool
    Light Boolean (switch) variable, it uses at least 1 bit (one eighth byte) to store, prefer to use this instead of var for Boolean variables  
    In the internal implementation of eudplib, every 32 EUDLightBool share one EUDLightVariable  
    Boolean (switch) can only represent two states, 1 means Set, 0 means Cleared, the default initial value is Cleared  

    ```JavaScript
    object EUDLightBool {
        // Compile-time constant functions
        function getValueAddr() {}        

        // Regular conditions
        function IsSet(){}      // The current switch is in the set state
        function IsCleared(){}  // The current switch is in the cleared state

        // Regular actions
        function Set(){}        // Set to on
        function Clear(){}      // Set to off
        function Toggle(){}     // Toggle switch state
    };
    ```

    Example

    ```JavaScript
    const b = EUDLightBool(); // Default initial value is Cleared
    DoActions(
        b.Set(),
        b.Clear(),
        b.Toggle(),
    );
    if ( b.IsSet() ) {
        simpleprint("b is set");
    }
    if ( b.IsCleared() ) {
        simpleprint("b is cleared");
    }
    ```

<br />

- ### EUDArray

    Light static array container, it can be declared using `[...]` syntax, the size cannot be dynamically changed.

    ```JavaScript
    object EUDArray {
        function constructor(size) {}
        const length;
    };
    ```

    Example

    ```JavaScript
    const a = EUDArray(10); // Declare an array of size 10 (index 0~9)
    a[0] = 29; // Set the element at index 0 of array a to 29

    println("Array size:{} [0] value:{}", a.length, a[0]); // Array size: 10 [0] value: 29

    const b = [3, 2, 1]; // Declare an array of size 3 (index 0~2) and initialize to b[0] = 3; b[1] = 2; b[2] = 1;

    const c = [list(3, 2, 1), 4, list(5, 6)]; // Declare an array of size 6 (index 0~5) and initialize to b[0] = 3; b[1] = 2; b[2] = 1; b[3] = 4; b[4] = 5; b[5] = 6; 
    ```

<br />

- ### EUDVArray
    Static array container implemented using virtual triggers, it can be declared using `VArray(...)` syntax, the size cannot be dynamically changed.  
    
    EUDVArray container supports the static setting of the reference type of the values it contains.    

    It has faster access speed when the array index is a variable.  

    ```JavaScript
    object EUDVArray {
        function constructor(size : py_int, basetype : type) : _EUDVArrayClass {}
    };

    object _EUDVArray {
        function constructor(vars : list) {}
        const length;
    }
    ```

    Example

    ```C#
    const a = EUDVArray(4)(list(1, 2, 3, 4)); // Declare an array of size 4 and initialize to a[0] = 1; a[1] = 2; a[2] = 3; a[3] = 4;

    const b = VArray(1, 2, 3, 4); // Same as above

    const c = VArray(list(1, 2, 3, 4)); // Same as above

    const d = VArray(list(1, 2), list(3, 4)); // Same as above

    const d = EUDVArray(4)(); // Declare an array of size 4, equivalent to VArray(0, 0, 0, 0);
    foreach (i : py_range(4)) {
        d[i] = i + 1;
    }

    // Declare a 4 x 2 two-dimensional array
    const e = EUDVArray(4, EUDVArray(2))(list(VArray(5, 6), VArray(7, 8), VArray(9, 10), VArray(11, 12)));
    var a = e[2][1]; // Supported in euddraft 0.9.9.8
    println("e[2][1] == {}", a); // e[2][1] == 10
    ```

<br />

- ### PVariable

    Player variable, which is actually another representation of `EUDVArray(8)()`, that is, an array that stores different values for each player, with a maximum of 8 players in StarCraft.  

    ```JavaScript
    object PVariable {
        const length;
    };
    ```

    Example

    ```JavaScript
    // They are equivalent
    const pv1 = PVariable();
    const pv2 = EUDVArray(8)();
    ```

<br />

- ### EUDVArrayReader

    For traversing EUDVArray

    ```JavaScript
    object EUDVArrayReader {
        function seek(varr_ptr, varr_epd, eudv, acts) {}
        function read(acts) {}
    }
    ```

<br />

- ### EUDDeque

    Static double-ended queue container implemented using virtual triggers, EUDDeque is a runtime iterator type.  
  
    ```JavaScript
    object EUDDeque {
        function constructor(size : py_int, basetype : type) : _EUDDequeClass {}
    };

    object _EUDDeque {
        function constructor() {}
        function append(arg) {}
        function appendleft(arg) {}
        function pop() {}
        function popleft() {}
        function clear() {}
        function empty() {}
        const length;
    };
    ```

    Example

    ```JavaScript
    const dq = EUDDeque(10)();

    // `.length` : Get the current number of elements in the deque
    println("Number of elements in deque {}", dq.length);

    // `.append(x)` : Add x to the far right of the deque
    dq.append(10);

    // `.pop()` : Pop the element at the far right of the deque (remove and return), you need to determine if there are elements in the deque first, if there are no elements inside, the behavior of using this method directly is undefined.
    println("The value at the far right of the deque pops out {}", dq.pop());

    // `.appendleft(x)` : Add x to the far left of the deque
    dq.appendleft(13);

    // `.popleft()` : Pop the element at the far left of the deque (remove and return), you need to determine if there are elements in the deque first, if there are no elements inside, the behavior of using this method directly is undefined.
    println("The value at the far left of the deque pops out {}", dq.popleft());

    // `.clear()` : Clear the deque
    dq.clear();

    // `.empty()` : Determine if the number of elements in the current deque is 0
    if (dq.empty()) {
        println("Deque is empty");
    }

    ```

<br />

- ### StringBuffer

    Static in-memory string buffer operation type

    ```JavaScript
    object StringBuffer {
        function constructor(content : py_str | py_bytes) {}
        function constructor(len : py_int) {}
        function append(*args) {}
        function appendf(format_string, *args) {}
        function insert(index, *args) {}
        function insertf(index, format_string, *args) {}
        function delete(start, length=1) {}
        function Display() {}
        function DisplayAt(line) {}
        function print(*args) {}
        function printf(format_string, *args) {}
        function printfAt(line, format_string, *args) {}
        function Play() {}
        function fadeIn(*args, line=-1, color=None, wait=1, reset=True, tag=None) {}
        function fadeOut(*args, line=-1, color=None, wait=1, reset=True, tag=None) {}
        function fadeInf(format_string, *args, line=-1, color=None, wait=1, reset=True, tag=None) {}
        function fadeOutf(format_string, *args, line=-1, color=None, wait=1, reset=True, tag=None) {}
        function length();
        const StringIndex;
        const epd;
    };
    ```

    Except for the initialization method, all methods of the StringBuffer object are asynchronous methods and only take effect on the machine where `Current Player == Local Player`.

    ```JavaScript
    const buf = StringBuffer(64); // Initialize buffer size

    setcurpl(P1); // Set current player to P1
    buf.insert(0, "Information displayed to player 1");  // This line will only modify buf on P1's machine because the current player is P1

    if (getuserplayerid() == $P2) {     // The local player is P2
        buf.insert(0, "This line of code is useless"); // The local player is P2 but the current player is P1 so this line of code does not work
    }

    setcurpl(P2); // Set current player to P2
    buf.insert(0, "Information displayed to player 2");  // This line will only modify buf on P2's machine because the current player is P2

    setcurpl(P1);
    buf.Display(); // Display "Information displayed to player 1" to player 1

    setcurpl(P2);
    buf.Display(); // Display "Information displayed to player 2" to player 2
    ```

- #### StringBuffer

    - `StringBuffer`(content)  
        If [content] is a string or byte string, a StringBuffer object is initialized with that string or byte string.  
        If [content] is an integer, a StringBuffer object is initialized with [content] as the size.  
        [content] is an optional parameter, the default is 218.  

    ```JavaScript
    const s1 = StringBuffer();         // StringBuffer object with size 218, initial content is 218 * \r
    const s2 = StringBuffer(64);       // StringBuffer object with size 64, initial content is 64 * \r
    const s3 = StringBuffer("havonz"); // StringBuffer object with size 6, initial content is "havonz"
    ```


- #### .insert

    - `.insert`(index, *args)  
        Convert the variable arguments [*args] into strings and insert them in order into the buffer of the `current player`'s machine StringBuffer object at position `[index] * 4` (this cannot be used if the index is not a multiple of 4).
    
    - `.insertf`(index, format_string, *args)  
        Format the variable arguments [*args] using [format_string] and insert into the buffer of the `current player`'s machine StringBuffer object at position `[index] * 4` (this cannot be used if the index is not a multiple of 4).


    ```JavaScript
    const s1 = StringBuffer();
    s1.insert(0, "havonz");
    s1.insert(1, "0");
    s1.Display(); // havo0
    ```


- #### .append

    - `.append`(*args)  
        Convert the variable arguments [*args] into strings and append them in order to the end of the string in the buffer of the `current player`'s machine StringBuffer object.
    
    - `.appendf`(format_string, *args)  
        Format the variable arguments [*args] using [format_string] and append to the end of the string in the buffer of the `current player`'s machine StringBuffer object.

    ```JavaScript
    const s1 = StringBuffer();
    setcurpl(getuserplayerid());
    s1.insert(0);
    s1.append("Hello!");
    s1.appendf("{}{}", PColor(getuserplayerid()), PName(getuserplayerid()) );
    s1.Display();
    ```


- #### .delete

    - `.delete`(start, length=1)  
        Delete `[length] * 4` bytes from the `[start] * 4` index position of the StringBuffer object on the `current player`'s machine (this cannot be used if the index is not a multiple of 4).  


- #### .Display

    - `.Display()`  
        Print the string in the StringBuffer buffer to the bottom line of the scrolling message on the `current player`'s screen.  

    - `.DisplayAt`(line)  
        Print the string in the StringBuffer buffer to the [line]th line from top to bottom of the scrolling message on the `current player`'s screen.  

    ```JavaScript
    const s1 = StringBuffer();
    setcurpl(getuserplayerid());
    s1.insert(0, "Hello! StarCraft");
    s1.DisplayAt(0); // Output to the top line
    s1.Display();    // Output to the bottom line
    ```


- #### .print

    - `.print`(*args)  
        Use the current StringBuffer to print multiple arguments [*args] sequentially to the next line of the scrolling message on the `current player`'s screen, scrolling the bottom message up.  

    - `.printf`(formatstring, *args)  
        Use the current StringBuffer to format print multiple arguments [*args] to the next line of the scrolling message on the `current player`'s screen using the [format_string] format, scrolling the bottom  

    - `.printfAt`(line, formatstring, *args)  
        Use the current StringBuffer to format print multiple arguments [*args] to the [line]th line (range 0~10) from top to bottom of the scrolling message on the `current player`'s screen using the [format_string] format.  

    ```JavaScript
    const s1 = StringBuffer();
    setcurpl(getuserplayerid());
    s1.print("Hello! StarCraft"); // Scroll out a message at the bottom
    s1.printf("Hello!{}{}", PColor(getuserplayerid()), PName(getuserplayerid()) ); // Scroll up the previous message and scroll out this message
    s1.printfAt(0, "Hello!{}{}", PColor(getuserplayerid()), PName(getuserplayerid()) ); // Print this message from the top line
    ```


- #### .Play

    - `.Play()`  
        Use the content of the StringBuffer object on the `current player`'s machine as a sound file name and play that sound file.  
        When the target sound file contains localized sounds, the dynamically concatenated file name using StringBuffer will be unable to play.  

    ```JavaScript
    setcurpl(P1);
    buf.insert(0, "sound\\Zerg\\Devourer\\");
    buf.append("ZDvPss00.WAV\0");
    buf.Display();    // Output "sound\Zerg\Devourer\ZDvPss00.WAV" on the next line of the screen of player 1
    buf.DisplayAt(9); // Output "sound\Zerg\Devourer\ZDvPss00.WAV" on the tenth line of the screen of player 1 
    buf.Play();       // Find the wav pointed to by the text and play it on player 1's computer

    StringBuffer("sound\\terran\\advisor\\tadupd04.wav").Play(); // nuclear launch detected.
    ```


- #### .fade

    - `.fadeIn`(*args, line=0, color=None, wait=1, reset=true, tag=None)  
        Make [*args] combine into a text gradually appearing from [line] line in [clolor] color, with [wait] frames interval, whether to reset [reset], special effect text tag [tag], call repeatedly, return non-0 means the special effect is not completed and needs to continue calling, return 0 means the special effect is completed.  

    - `.fadeOut`(*args, line=0, color=None, wait=1, reset=true, tag=None)  
        Make [*args] combine into a text gradually disappearing from [line] line in [clolor] color, with [wait] frames interval, whether to reset [reset], special effect text tag [tag], call repeatedly, return non-0 means the special effect is not completed and needs to continue calling, return 0 means the special effect is completed.  

    - `.fadeInf`(format_string, *args, line=0, color=None, wait=1, reset=true, tag=None)  
        Make [*args] format into a text using [format_string] gradually appearing from [line] line in [clolor] color, with [wait] frames interval, whether to reset [reset], special effect text tag [tag], return non-0 means the special effect is not completed and needs to continue calling, return 0 means the special effect is completed.  

    - `.fadeOutf`(format_string, *args, line=0, color=None, wait=1, reset=true, tag=None)  
        Make [*args] format into a text using [format_string] gradually disappearing from [line] line in [clolor] color, with [wait] frames interval, whether to reset [reset], special effect text tag [tag], return non-0 means the special effect is not completed and needs to continue calling, return 0 means the special effect is completed.  

    ```JavaScript
    function fadeInAndFadeOutTextOnce() {
        const buf = StringBuffer(128);
        const onceWait = EUDLightVariable(0);

        if (getcurpl() != getuserplayerid()) {
            return;
        }

        if (onceWait >= 10000) {
            return;
        }

        const text = py_str("\x13\x04lose\x19humanity\n\x13\x04lose\x19a lot\n\x13\x04lose\x19beast\n\x13\x04lose\x19all\n"); 

        const tecolor = 4, 2, 0x1E, 5, 0;

        if (onceWait <= 0) {
            if ( 0 != buf.fadeIn(text, line = 3, color = tecolor, wait = 2, tag = py_str("fadeInEff")) ) {
                return;
            }
        }

        if (onceWait <= 100) {
            DoActions(onceWait.AddNumber(1));
            return;
        }

        TextFX_SetTimer("fadeInEff", SetTo, 0);
        TextFX_Remove("fadeInEff");

        if ( 0 != buf.fadeOut(text, line = 3, color = tecolor, wait = 2, tag = py_str("fadeOutEff")) ) {
            return;
        }

        TextFX_SetTimer("fadeOutEff", SetTo, 0);
        TextFX_Remove("fadeOutEff");
        DoActions(onceWait.SetNumber(10000)); /* Done */
    }

    function beforeTriggerExec() {
        const cp = getcurpl();

        setcurpl(getuserplayerid());
        fadeInAndFadeOutTextOnce();

        setcurpl(cp);
    }
    ```


<br />

- ### Db

    Static memory bytes object type

    ```JavaScript
    object Db {
    function constructor(content) {}
    function GetDataSize() {}
    };
    ```

    Support initializing a memory byte data using integers, strings, bytes

    `Db("string")` is equivalent to `Db(b"string\0")`(UTF-8)

    ```JavaScript
    const buf1 = Db(b"string\0"); // Db(b"string\0")
    const buf2 = Db("string");    // Db(b"string\0")
    const buf3 = Db(5);           // Db(b"\0\0\0\0\0")
    ```

<br />

- ### EUDByteStream

    Memory byte stream operation object type

    ```JavaScript
    object EUDByteStream {
        function seekepd(epd) {}
        function seekoffset(ptr) {}
        function copyto(stream : EUDByteStream) {}
        function readbyte() {}
        function writebyte(byte) {}
    }
    ```

    ```JavaScript
    const buf = Db(b"\0uck fu\0k fuck");
    sprintf(buf, "908 + 8 = {}", 908 + 8);
    StringBuffer().printAt(6, ptr2s(buf));
    const stream = EUDByteStream();
    stream.seekoffset(buf);
    StringBuffer().printAt(7, stream.readbyte());
    stream.seekoffset(buf);
    stream.writebyte(97);
    stream.writebyte(98);
    stream.writebyte(99);
    StringBuffer().printAt(8, ptr2s(buf));
    ```

<br />

- ### ~~CPString~~

    **Deprecated**
    CPTricks optimized string buffer operation object type

    ```JavaScript
    object CPString {
    function constructor(content) {}
    function Display() {}
    function GetVTable() {}
    };
    ```

    ```JavaScript
    const s1 = CPString("a string");
    const s2 = CPString(b"stringstringstring");
    const s3 = CPString(64);
    ```

<br />

- ### ~~DBString~~

    **Deprecated**
    Static memory string object type

    ```JavaScript
    object DBString {
    function constructor(content) {}
    function GetStringMemoryAddr() {}
    function Display() {}
    function Play() {}
    };
    ```

    ```JavaScript
    const s = DBString("a very long string\0a very long string");
    const buf = s.GetStringMemoryAddr();
    s.Display();
    sprintf(buf, "908 + 8 = {}", 908 + 8);
    s.Display();
    ```

    

  

  

  






---


# Built-in Extended Object Types

Object types related to game content  

Reference:   
[https://cafe.naver.com/edac/120138](https://cafe.naver.com/edac/120138)

<br />

- [Extended Object Types](#extended-object-types)
    - [CUnit](#cunit)
    - [UnitGroup](#unitgroup)
    - [CSprite](#csprite)

<br />

## Extended Object Types

- ### CUnit

    EPDCUnitMap is another way to write CUnit  
    Unit instance operation object, which can operate a specific unit on the map. In the editor, Unit actually refers to the unit type instead of the unit instance.  
    CUnit is a reference type, and the unit instance it operates on belongs to `data that needs to be synchronized`.  

    ```JavaScript
    object CUnit {
        function constructor(epd) {}
        static function from_read(epd) {}
        static function from_ptr(ptr) {}
    
        function set_color(Player : TrgPlayer){}
        function reset_buildq(){}
        function setloc(Location : TrgLocation){}
        function is_burrowed(){}
        function is_in_transport(){}
        function is_in_building(){}
        function is_air(){}
        function is_hallucination(){}
        function is_completed(){}
        function is_dying(){}
        function die(){}
        function set_speed_upgrade(){}
        function clear_speed_upgrade(){}
        function set_air(){}
        function set_ground(){}
        function set_invincible(){}
        function clear_invincible(){}
        function remove_collision(){}
        function set_hallucination(){}
        function clear_hallucination(){}
        function power(){}
        function unpower(){}
        function set_noclip(){}
        function clear_noclip(){}
        function set_gathering(){}
        function clear_gathering(){}
        function check_status_flag(Value){}
        function check_status_flag(Value, Mask){}
        function set_status_flag(Value){}
        function set_status_flag(Value, Mask){}
        function clear_status_flag(Value){}

        var prev;// CUnitMember(0x000)
        var next;// CUnitMember(0x004)  //link
        var hp;// Member(0x008, MemberKind.DWORD)  //displayed value is ceil(healthPoints/256)
        var sprite;// CSpriteMember(0x00C)
        var moveTargetPos;// Member(0x010, MemberKind.POSITION)
        var moveTargetX;// Member(0x010, MemberKind.POSITION_X)
        var moveTargetY;// Member(0x012, MemberKind.POSITION_Y)
        var moveTarget;// CUnitMember(0x014)
        var moveTargetUnit;// CUnitMember(0x014)
        var nextMovementWaypoint;// Member(0x018, MemberKind.POSITION)  //The next way point in the path the unit is following to get to its destination. Equal to moveToPos for air units since they don't need to navigate around buildings.
        var nextTargetWaypoint;// Member(0x01C, MemberKind.POSITION)  //The desired position
        var movementFlags;// MovementFlags(0x020, MemberKind.BYTE)
        var currentDirection1;// Member(0x021, MemberKind.BYTE)  //current direction the unit is facing
        var turnRadius;// Member(0x022, MemberKind.BYTE)  //flingy
        var velocityDirection1;// Member(0x023, MemberKind.BYTE)  //usually only differs from the currentDirection field for units that can accelerate and travel in a different direction than they are facing. For example Mutalisks can change the direction they are facing faster than then can change the direction they are moving.
        var flingyID;// Member(0x024, MemberKind.FLINGY)
        var unknown0x26;// Member(0x026, MemberKind.BYTE)
        var flingyMovementType;// Member(0x027, MemberKind.BYTE)
        var pos;// Member(0x028, MemberKind.POSITION)  //Current position of the unit
        var posX;// Member(0x028, MemberKind.POSITION_X)
        var posY;// Member(0x02A, MemberKind.POSITION_Y)
        var haltX;// Member(0x02C, MemberKind.DWORD)
        var haltY;// Member(0x030, MemberKind.DWORD)
        var topSpeed;// Member(0x034, MemberKind.DWORD)
        var currentSpeed1;// Member(0x038, MemberKind.DWORD)
        var currentSpeed2;// Member(0x03C, MemberKind.DWORD)
        var currentVelocityX;// Member(0x040, MemberKind.DWORD)
        var currentVelocityY;// Member(0x044, MemberKind.DWORD)
        var acceleration;// Member(0x048, MemberKind.WORD)
        var currentDirection2;// Member(0x04A, MemberKind.BYTE)
        var velocityDirection2;// Member(0x04B, MemberKind.BYTE)  //pathing related
        var playerID;// Member(0x04C, MemberKind.TRG_PLAYER)
        var owner;// Member(0x04C, MemberKind.TRG_PLAYER)
        var orderID;// Member(0x04D, MemberKind.UNIT_ORDER)
        var order;// Member(0x04D, MemberKind.UNIT_ORDER)
        var orderState;// Member(0x04E, MemberKind.BYTE)
        var orderSignal;// Member(0x04F, MemberKind.BYTE)
        var orderUnitType;// Member(0x050, MemberKind.TRG_UNIT)
        var unknown0x52;// Member(0x052, MemberKind.WORD)  //2-byte padding
        var cooldown;// Member(0x054, MemberKind.DWORD)
        var orderTimer;// Member(0x054, MemberKind.BYTE)
        var gCooldown;// Member(0x055, MemberKind.BYTE)
        var aCooldown;// Member(0x056, MemberKind.BYTE)
        var spellCooldown;// Member(0x057, MemberKind.BYTE)
        var groundWeaponCooldown;// Member(0x055, MemberKind.BYTE)
        var airWeaponCooldown;// Member(0x056, MemberKind.BYTE)
        var orderTargetPos;// Member(0x058, MemberKind.POSITION)  //ActionFocus
        var orderTargetXY;// Member(0x058, MemberKind.POSITION)
        var orderTargetX;// Member(0x058, MemberKind.POSITION_X)
        var orderTargetY;// Member(0x05A, MemberKind.POSITION_Y)
        var orderTarget;// CUnitMember(0x05C)
        var orderTargetUnit;// CUnitMember(0x05C)
        var shield;// Member(0x060, MemberKind.DWORD)
        var unitID;// Member(0x064, MemberKind.TRG_UNIT)
        var unitType;// Member(0x064, MemberKind.TRG_UNIT)
        var unknown0x66;// Member(0x066, MemberKind.WORD)  //2-byte padding
        var prevPlayerUnit;// CUnitMember(0x068)
        var nextPlayerUnit;// CUnitMember(0x06C)
        var subUnit;// CUnitMember(0x070)
        var orderQueueHead;// UnsupportedMember(0x074, MemberKind.DWORD)  //COrder
        var orderQueueTail;// UnsupportedMember(0x078, MemberKind.DWORD)
        var autoTargetUnit;// CUnitMember(0x07C)
        var connectedUnit;// CUnitMember(0x080)  //larva, in-transit, addons
        var orderQueueCount;// Member(0x084, MemberKind.BYTE)  //may be count in addition to first since can be 2 when 3 orders are queued
        var orderQueueTimer;// Member(0x085, MemberKind.BYTE)  //Cycles down from from 8 to 0 (inclusive). See also 0x122.
        var unknown0x86;// Member(0x086, MemberKind.BYTE)
        var attackNotifyTimer;// Member(0x087, MemberKind.BYTE)  //Prevent "Your forces are under attack." on every attack
        var prevUnitType;// UnsupportedMember(0x088, MemberKind.TRG_UNIT)  //zerg buildings while morphing
        var lastEventTimer;// UnsupportedMember(0x08A, MemberKind.BYTE)
        var lastEventColor;// UnsupportedMember(0x08B, MemberKind.BYTE)  //17 : was completed (train, morph), 174 : was attacked
        var unknown0x8C;// Member(0x08C, MemberKind.WORD)  // might have originally been RGB from lastEventColor
        var rankIncrease;// Member(0x08E, MemberKind.BYTE)
        var killCount;// Member(0x08F, MemberKind.BYTE)
        var lastAttackingPlayer;// Member(0x090, MemberKind.TRG_PLAYER)
        var secondaryOrderTimer;// Member(0x091, MemberKind.BYTE)
        var AIActionFlag;// Member(0x092, MemberKind.BYTE)
        var userActionFlags;// Member(0x093, MemberKind.BYTE)  //2 : issued an order, 3 : interrupted an order, 4 : hide self before death (self-destruct?)
        var currentButtonSet;// Member(0x094, MemberKind.WORD)
        var isCloaked;// Member(0x096, MemberKind.BOOL)
        var movementState;// Member(0x097, MemberKind.BYTE)
    };
    ```

    ```JavaScript
    const unit = CUnit.cast(v)        // Convert function argument or return value to CUnit object  
    const unit = CUnit(EPD)           // Create CUnit object from structure offset EPD value   
    const unit = CUnit(EPD, ptr=ptr)  // Create CUnit object from structure offset EPD value and ptr value
    const unit = CUnit.from_read(EPD) // Read from the memory address storing EPD value and create CUnit object. If the address is empty, unit is 0   
    const unit = CUnit.from_ptr(ptr)  // Calculate EPD from ptr value and create CUnit type. Cache ptr value at call location to avoid recalculating EPD
    const unit = CUnit(EPD).subUnit   // CUnit type member of CUnit instance
    ```

    ```JavaScript
    // Example: Increase resource collection over 256
    const bonusMineral = PVariable(list(492, 0, 0, 0, 0, 0, 0, 0));  // P1 is 492 + 8 = collect up to 500 mineral  
    const bonusGas = PVariable(list(992, 0, 0, 0, 0, 0, 0, 0));  // P1 is 992 + 8 = collect up to 1000 gas
    function loopUnit() {
        foreach(unit : EUDLoopCUnit()) {
            epdswitch(unit + 0x64/4, 255) {  // Unit type  
            case $U("Mineral Field (Type 1)"), $U("Mineral Field (Type 2)"), $U("Mineral Field (Type 3)"):
                // Several workers collect a mineral patch at the same time 
                unit.gatherQueueCount = 0;
                unit.nextGatherer = 0;
                break;
            case $U("Terran SCV"), $U("Zerg Drone"), $U("Protoss Probe"):
                const worker = unit;
                // If the worker is not carrying anything and has extra resources, provide extra resources
                // worker.unknown0x66 = Extra collection amount (mineral or gas)
                // worker.resourceType = Resource type (1 = mineral, 2 = gas) 
                // worker.connectedUnit = Resource (mineral patch/gas building) address
                if(worker.resourceCarryAmount == 0 && worker.unknown0x66 >= 1) {
                    if(worker.resourceType == 1) {
                        SetResources(worker.owner, Add, worker.unknown0x66, Ore);
                    } else if(worker.resourceType == 2) {
                        SetResources(worker.owner, Add, worker.unknown0x66, Gas);
                    }
                    worker.resourceType = 0;
                    worker.unknown0x66 = 0;
                }
                epdswitch(worker + 0x4D/4, 0xFF00) {  // Order
                case EncodeUnitOrder("Harvesting Minerals") * 256, EncodeUnitOrder("Enter/Exit Gas Mine") * 256: {
                    worker.connectedUnit = worker.orderTarget;  // Store the mineral address in unused space
                    // Indicates mineral/gas 
                    worker.resourceType = 1 + l2v(worker.order == EncodeUnitOrder("Enter/Exit Gas Mine"));
                    break;
                } case EncodeUnitOrder("Reset Collision (Harvester&amp;Mine)") * 256: {
                    // Operates after mining minerals or gas
                    if(worker.connectedUnit >= 1 && worker.resourceType >= 1 && worker.resourceType <= 2) {
                        const player = worker.owner;
                        const bonusAmount = (worker.resourceType == 1) ? bonusMineral[player] : bonusGas[player];
                        const targetResource = worker.connectedUnit;  // Mineral patch/gas building CUnit!
                        const resourceAmount = targetResource.resourceAmount;
                        // If the remaining amount of mineral/gas building is less than the extra collection amount
                        if (resourceAmount < bonusAmount) {
                            // Collect all remaining amounts
                            worker.unknown0x66 = resourceAmount;
                            targetResource.resourceAmount = 0;
                        } else {
                            // If the mineral patch/gas building has enough extra collection amounts, collect more
                            worker.unknown0x66 = bonusAmount;
                            targetResource.resourceAmount -= bonusAmount;
                        }
                    }
                }
                case EncodeUnitOrder("Can Harvest Minerals") * 256:
                    if(worker.orderState == 2) {
                        worker.order = py_str("Move to Harvest Minerals");
                        worker.orderState = 1;
                    }
                    break;
                }
                break;
            }
        }
    }
    ```


- ### UnitGroup

    UnitGroup is an optimized unit instance container after applying CPTricks.  

    ```JavaScript
    object GUnit {
        function remove(){}           // Remove itself from the UnitGroup you belong to
        const dying : EUDGUnitIter;   // It is not actually an iterator. If the unit is alive, the foreach code block will not execute. If the unit dies, after executing the code block in foreach, the dead unit will remove itself from the UnitGroup it belongs to.
    }

    object UnitGroup {
        function add(epd) {}
        const cp_loop : EUDGUnitIter; // cp_loop returns an iterator that iterates over all unit instances in the container. For now, let's call this unit instance type GUnit. GUnit has a remove method to remove itself from the UnitGroup it belongs to
    };
    ```

    ```JavaScript
    // epScript example

    // UnitGroup Declaration
    const zerglings = UnitGroup(1000);
    // max capacity = 1000, will use CPTrick

    // Register Unit
    zerglings.add(epd);

    // Loop UnitGroup
    foreach(unit : zerglings.cploop) {
        // Run Triggers on **any** zerglings (alive or dead)
        foreach(dead : unit.dying) {
            // Run Triggers on dead zerglings
        }  // <- dead zergling will be removed at end of *dying* block
        // Run Triggers on alive zerglings
    }

    // example usage
    function afterTriggerExec() {
        const zerglings = UnitGroup(1000);
        foreach(cunit : EUDLoopNewCUnit()) {
            epdswitch(cunit + 0x64/4, 255) {
            case $U("Zerg Zergling"):
                zerglings.add(epd);
                break;
            }
        }
        foreach(unit : zerglings.cploop) {
            foreach(dead : unit.dying) {
                // spawn Infested Terran when zergling dies
                dead.move_cp(0x4C / 4);  // Owner
                const owner = bread_cp(0, 0);
                dead.move_cp(0x28 / 4);  // Unit Position
                const x, y = posread_cp(0);

                setloc("loc", x, y);
                CreateUnit(1, "Infested Terran", "loc", owner);
            }
        }
    }
    ```

- ### CSprite

    Sprite instance operation object type

    ```Python
    class CSpriteFlags(EnumMember):
        DrawSelCircle = Flag(0x01)  # Draw selection circle
        AllySel1 = Flag(0x02)
        AllySel2 = Flag(0x04)
        Selected = Flag(0x08)  # Draw HP bar, Selected
        Flag4 = Flag(0x10)
        Hidden = Flag(0x20)  # Hidden
        Burrowed = Flag(0x40)  # Burrowed
        IscriptCode = Flag(0x80)  # Iscript unbreakable code section

    class CSprite(EPDOffsetMap):
        __slots__ = "_ptr"
        prev = CSpriteMember(0x00)
        next = CSpriteMember(0x04)
        sprite = Member(0x08, MemberKind.SPRITE)
        playerID = Member(0x0A, MemberKind.TRG_PLAYER)  # officially "creator"
        # 0 <= selectionIndex <= 11. Index in the selection area at bottom of screen.
        selectionIndex = Member(0x0B, MemberKind.BYTE)
        # Player bits indicating the visibility for a player (not hidden by the fog-of-war)
        visibilityFlags = Member(0x0C, MemberKind.BYTE)
        elevationLevel = Member(0x0D, MemberKind.BYTE)
        flags = CSpriteFlags(0x0E, MemberKind.BYTE)
        selectionTimer = Member(0x0F, MemberKind.BYTE)
        index = Member(0x10, MemberKind.WORD)
        unknown0x12 = Member(0x12, MemberKind.BYTE)
        unknown0x13 = Member(0x13, MemberKind.BYTE)
        pos = Member(0x14, MemberKind.POSITION)
        posX = Member(0x14, MemberKind.POSITION_X)
        posY = Member(0x16, MemberKind.POSITION_Y)
        mainGraphic = Member(0x18, MemberKind.DWORD)  # officially "pImagePrimary"
        imageHead = Member(0x1C, MemberKind.DWORD)
        imageTail = Member(0x20, MemberKind.DWORD)

        def __init__(self, epd: int_or_var, *, ptr: int_or_var | None = None) -> None:

        @classmethod
        def cast(cls: type[T], _from: int_or_var) -> T:

        @classmethod
        def from_ptr(cls: type[T], ptr: int_or_var) -> T:

        @classmethod
        def from_read(cls: type[T], epd) -> T:

        @property
        def ptr(self) -> int | c.EUDVariable:
    ```

---


# Built-in Functions

<br />

- [Conditions and Actions](#conditions-and-actions)
    - [Normal Condition Functions](#normal-condition-functions)
        - [Accumulate](#accumulate)
        - [Bring](#bring)
        - [Command](#command)
        - [CountdownTimer](#countdowntimer)
        - [Deaths](#deaths)
        - [Memory](#memory)
        - [Kills](#kills)
        - [ElapsedTime](#elapsedtime)
        - [LeastKills/MostKills](#leastkillsmostkills)
        - [LeastResources/MostResources](#leastresourcesmostresources)
        - [Opponents](#opponents)
        - [Score](#score)
        - [Switch](#switch)
        - [~~Always/Never~~](#alwaysnever)
    - [Extended Condition Functions](#extended-condition-functions)
        - [IsUserCP](#isusercp)
        - [Is64BitWireframe](#is64bitwireframe)
    - [Normal Action Functions](#normal-action-functions)
        - [CenterView](#centerview)
        - [CreateUnit](#createunit)
        - [Defeat/Victory/Draw](#defeatvictorydraw)
        - [DisplayText](#displaytext)
        - [GiveUnits](#giveunits)
        - [KillUnit](#killunit)
        - [LeaderBoard](#leaderboard)
        - [MinimapPing](#minimapping)
        - [ModifyUnit](#modifyunit)
        - [MoveLocation](#movelocation)
        - [MoveUnit](#moveunit)
        - [MuteUnitSpeech/UnMuteUnitSpeech](#muteunitspeechunmuteunitspeech)
        - [Order](#order)
        - [PauseGame/UnpauseGame](#pausegameunpausegame)
        - [PauseTimer/UnpauseTimer](#pausetimerunpausetimer)
        - [PlayWAV](#playwav)
        - [~~PreserveTrigger~~](#preservetrigger)
        - [RemoveUnit](#removeunit)
        - [RunAIScript](#runaiscript)
        - [SetAllianceStatus](#setalliancestatus)
        - [SetCountdownTimer](#setcountdowntimer)
        - [SetDeaths](#setdeaths)
        - [SetMemory](#setmemory)
        - [SetDoodadState](#setdoodadstate)
        - [SetInvincibility](#setinvincibility)
        - [SetMissionObjectives](#setmissionobjectives)
        - [SetNextScenario](#setnextscenario)
        - [SetResources](#setresources)
        - [SetScore](#setscore)
        - [SetSwitch](#setswitch)
        - [TalkingPortrait](#talkingportrait)
        - [Transmission](#transmission)
        - [~~Wait~~](#wait)
    - [Extended Action Functions](#extended-action-functions)
        - [SetKills](#setkills)
        - [SetCurrentPlayer](#setcurrentplayer)
        - [AddCurrentPlayer](#addcurrentplayer)
        - [DisplayTextAll](#displaytextall)
        - [PlayWAVAll](#playwavall)
        - [MinimapPingAll](#minimappingall)
        - [CenterViewAll](#centerviewall)
        - [SetMissionObjectivesAll](#setmissionobjectivesall)
        - [TalkingPortraitAll](#talkingportraitall)
        - [SetNextPtr](#setnextptr)
- [Extended Functions](#extended-functions)
    - [Compile Time](#compile-time)
        - [Get Index](#get-index)
        - [list](#list)
        - [EUDCreateVariables](#eudcreatevariables)
        - [SetVariables](#setvariables)
        - [SCMD2Text](#scmd2text)
        - [unProxy](#unproxy)
        - [UnitProperty](#unitproperty)
        - [GetPropertyIndex](#getpropertyindex)
        - [GetPlayerInfo](#getplayerinfo)
        - [EUDRegisterObjectToNamespace](#eudregisterobjecttonamespace)
        - [GetEUDNamespace](#geteudnamespace)
        - [MPQAddFile](#mpqaddfile)
        - [MPQAddWave](#mpqaddwave)
    - [Compile-time Python Macros](#compile-time-python-macros)
        - [py_print](#py_print)
        - [py_list](#py_list)
        - [py_open](#py_open)
        - [py_eval](#py_eval)
        - [py_str](#py_str)
        - [py_len](#py_len)
        - [py_enumerate](#py_enumerate)
        - [py_range](#py_range)
    - [Compile-time Bytes Conversion](#compile-time-bytes-conversion)
        - [b2i](#b2i)
        - [i2b](#i2b)
        - [u2b/b2u](#u2bb2u)
        - [UTF8 Encode/Decode](#utf8-encodedecode)
    - [General Functions](#general-functions)
        - [EPD](#epd)
        - [l2v](#l2v)
        - [parse](#parse)
        - [EUDFuncPtr](#eudfuncptr)
        - [getgametick](#getgametick)
    - [Trigger Construction Functions](#trigger-construction-functions)
        - [RawTrigger](#rawtrigger)
        - [Trigger](#trigger)
        - [PTrigger](#ptrigger)
        - [DoActions](#doactions)
        - [VProc](#vproc)
    - [Runtime Iterators](#runtime-iterators)
        - [EUDLoopPlayer](#eudloopplayer)
        - [EUDLoopRange](#eudlooprange)
        - [EUDLoopUnit](#eudloopunit)
    - [Display Text Functions](#display-text-functions)
        - [DisplayTextAt](#displaytextat)
        - [print](#print)
        - [GetGlobalStringBuffer](#getglobalstringbuffer)
        - [eprint](#eprint)
        - [TextFX](#textfx)
    - [Players Functions](#players-functions)
        - [getuserplayerid](#getuserplayerid)
        - [playerexist](#playerexist)
        - [Current Player](#current-player)
        - [PColor](#pcolor)
        - [PName](#pname)
        - [SetPName](#setpname)
        - [EUDPlayerLoop](#eudplayerloop)
    - [Location Functions](#location-functions)
        - [setloc](#setloc)
        - [addloc](#addloc)
        - [dilateloc](#dilateloc)
        - [getlocTL](#getloctl)
        - [setloc_epd](#setloc_epd)
    - [Memory Operation Functions](#memory-operation-functions)
        - [dwbreak](#dwbreak)
        - [read/write](#readwrite)
        - [read_epd/write_epd](#read_epdwrite_epd)
        - [add_epd/subtract_epd](#add_epdsubtract_epd)
        - [repmovsd_epd](#repmovsd_epd)
        - [dwepdread_epd](#dwepdread_epd)
        - [cunitread_epd](#cunitread_epd)
        - [posread_epd](#posread_epd)
        - [_cp Series](#_cp-series)
        - [readgen](#readgen)
        - [memcpy](#memcpy)
        - [memcmp](#memcmp)
        - [strcpy](#strcpy)
        - [strcmp](#strcmp)
        - [strlen](#strlen)
        - [strnstr](#strnstr)
        - [dbstr](#dbstr)
        - [ptr2s/epd2s](#ptr2sepd2s)
        - [hptr](#hptr)
        - [gettextptr](#gettextptr)
        - [dwpatch_epd](#dwpatch_epd)
        - [GetMapStringAddr](#getmapstringaddr)
        - [GetTBLAddr](#gettbladdr)
        - [settbl](#settbl)
    - [Math Functions](#math-functions)
        - [atan2](#atan2)
        - [sqrt](#sqrt)
        - [lengthdir](#lengthdir)
        - [pow](#pow)
        - [div](#div)
        - [rand](#rand)
        - [seed](#seed)
        - [randomize](#randomize)
    - [Bitwise Operation Functions](#bitwise-operation-functions)
        - [bitand](#bitand)
        - [bitor](#bitor)
        - [bitnot](#bitnot)
        - [bitxor](#bitxor)
        - [bitnand](#bitnand)
        - [bitnor](#bitnor)
        - [bitnxor](#bitnxor)
        - [bitlshift](#bitlshift)
        - [bitrshift](#bitrshift)
    - [QueueGameCommand Functions](#queuegamecommand-functions)
        - [QueueGameCommand](#queuegamecommand)
        - [QueueGameCommand_MinimapPing](#queuegamecommand_minimapping)
        - [QueueGameCommand_QueuedRightClick](#queuegamecommand_queuedrightclick)
        - [QueueGameCommand_Select](#queuegamecommand_select)
        - [QueueGameCommand_PauseGame](#queuegamecommand_pausegame)
        - [QueueGameCommand_ResumeGame](#queuegamecommand_resumegame)
        - [QueueGameCommand_RestartGame](#queuegamecommand_restartgame)
        - [QueueGameCommand_UseCheat](#queuegamecommand_usecheat)
        - [QueueGameCommand_TrainUnit](#queuegamecommand_trainunit)
        - [QueueGameCommand_MergeDarkArchon](#queuegamecommand_mergedarkarchon)
        - [QueueGameCommand_MergeArchon](#queuegamecommand_mergearchon)

<br />

## Conditions and Actions

- ### Normal Condition Functions

    Normal condition functions are functions encapsulated based on the conditions in classical triggers, just like the trigger conditions in ScmDraft2.  
    Any normal condition function will return a trigger condition expression constant (not a logical value). The concepts of `condition expression` and `condition expression result` need to be distinguished clearly.  
    If you need to use a variable to store the condition expression result, you should pass it into the condition list of a trigger or as an if syntax parameter. You can also use l2v to get the runtime result of the condition expression. See the following example:  
    
    ```JavaScript
    var vc0 = Accumulate(P1, AtLeast, 500, Ore);  // This is wrong!!! It does not return a logical value.
    const c1 = Accumulate(P1, AtLeast, 500, Ore); // This is ok, it returns a constant condition expression, which can be used as RawTrigger or Trigger conditions parameter   

    // Use a variable to store the logical value returned by the condition  
    var vc1 = 0;  
    Trigger(
        conditions = Accumulate(P1, AtLeast, 500, Ore),
        actions = vc1.SetNumber(1),  
    );
    var vc2 = l2v(Accumulate(P1, AtLeast, 500, Ore));
    ```

    <br />

    - #### **Accumulate**

        - `Accumulate`(player : TrgPlayer, AtLeast/AtMost/Exactly : TrgComparison, value, resourceType : TrgResource) : Condition   
            Compare whether the [resourceType] collected by [player] is [AtLeast/AtMost/Exactly] [value]

        Example

        ```JavaScript
        if ( Accumulate(P1, AtLeast, 500, Ore) ) {
            // If player 1 accumulate at least 500 ore minerals
        }
        ```


    <br />

    - #### **Bring**

        - `Bring`(player : TrgPlayer, AtLeast/AtMost/Exactly : TrgComparison, value, unitType : TrgUnit, location : TrgLocation) : Condition  
            Compare whether the number of [unitType] of [player] in [location] is [AtLeast/AtMost/Exactly] [value]  
            
            When the second parameter of Bring is AtMost, it will detect unfinished buildings, incubating creep tumors; it will not detect loaded units or units still in training; it will ignore the height setting of [location].  
            When the second parameter of Bring is AtLeast/Exactly, it will detect loaded units; it will not detect units still in training, unfinished buildings, or incubating creep tumors.  
            Bring cannot detect Scanner Sweep units or Map Revealers.  
            Units killed using KillUnit or KillUnitAt can still be detected by the Bring condition in the current frame; units removed using RemoveUnit or RemoveUnitAt can no longer be detected by the Bring condition in the current frame, and units previously killed using KillUnit or KillUnitAt will also no longer be detected by Bring.  

            [Bring Condition Bug](http://www.staredit.net/wiki/index.php?title=Bring_Condition_Bug)  

        Example

        ```JavaScript
        KillUnitAt(All, "Terran Marine", $L("Location 1"), P1); // Kill all Terran Marines of player 1 at Location 1. After this action, Bring can still detect player 1's Terran Marines at Location 1 in the current frame.   
        RemoveUnitAt(1, "Map Revealer", "Anywhere", P1);        // This action does not remove any units, but it refreshes all units previously killed using KillUnit or KillUnitAt in the current frame to ensure Bring no longer detects units killed in the current frame.    
        if (Bring(P1, AtLeast, 15, "Terran Marine", $L("Location 1"))) {
            // If the number of Terran Marines of player 1 at Location 1 is at least 15  
        }
        ```


    <br />

    - #### **Command**

        - `Command`(player : TrgPlayer, AtLeast/AtMost/Exactly : TrgComparison, value, unitType : TrgUnit) : Condition  
            Compare whether the number of [unitType] under the control of [player] on the map is [AtLeast/AtMost/Exactly] [value]  
            
            When the second parameter of Command is AtMost, it will detect loaded units, units still in training, unfinished buildings, incubating creep tumors.  
            When the second parameter of Command is AtLeast/Exactly, it will detect loaded units; it will not detect units still in training, unfinished buildings, or incubating creep tumors.  
            Command can detect Scanner Sweep units and Map Revealers.  
            Units killed or removed using KillUnit, KillUnitAt, RemoveUnit, RemoveUnitAt can still be detected by the Command condition in the current frame.  
        
        - `CommandMost`(unitType : TrgUnit) : Condition  
            Compare whether the [unitType] under the control of the current player on the map is more than any other player (including neutral players).  
        
        - `CommandLeast`(unitType : TrgUnit) : Condition  
            Compare whether the [unitType] under the control of the current player on the map is less than any other player (including neutral players).  
        
        - `CommandMostAt`(unitType : TrgUnit, location : TrgLocation) : Condition  
            Compare whether the [unitType] under the control of the current player at [location] is more than any other player (including neutral players).  
        
        - `CommandLeastAt`(unitType : TrgUnit, location : TrgLocation) : Condition  
            Compare whether the [unitType] under the control of the current player at [location] is less than any other player (including neutral players). 

        Example

        ```JavaScript
        const cp = getcurpl();  

        foreach (p: EUDLoopPlayer()) {  
            setcurpl(p);  
            if (Command(CurrentPlayer, AtMost, 0, "(buildings)")) { // When the second parameter of Command is AtMost, the statistics will include unfinished units/buildings  
                Defeat();     // If the number of buildings of the current player is at most 0, it is judged as defeat  
            }  

            if (CommandMost("Terran Marine")) {  
                println("Player {} has the most Terran Marines", p);  
            }  

            if (CommandLeast("Terran Marine")) {
                println("Player {} has the least Terran Marines", p);
            }  

            if (CommandMostAt("Terran Marine", $L("Location 1"))) {
                println("Player {} has the most Terran Marines at Location 1", p);
            }  

            if (CommandLeastAt("Terran Marine", $L("Location 1"))) {
                println("Player {} has the least Terran Marines at Location 1", p);
            }
        }  

        setcurpl(cp);
        ```


    <br />

    - #### **CountdownTimer**

        - `CountdownTimer`(AtLeast/AtMost/Exactly : TrgComparison, seconds) : Condition  
            Compare whether the remaining seconds of the countdown timer are [AtLeast/AtMost/Exactly] [seconds] game seconds  

        This condition should not use Exactly to compare because trigger polling does not occur every game second. One game second is 16 game frames, not equal to one real second.  

        Example

        ```JavaScript
        if ( CountdownTimer(AtMost, 1) ) {
            PauseTimer();
        }
        ```

    <br />

    - #### **Deaths**
        - `Deaths`(player : TrgPlayer, AtLeast/AtMost/Exactly : TrgComparison, value, unitType : TrgUnit) : Condition  
            Compare whether the death count of [unitType] of [player] is [AtLeast/AtMost/Exactly] [value]  

            <details>

            <summary>When [player] or [unitType] is out of range</summary>
            
            It is an EUD condition that compares whether the 32-bit unsigned integer stored at `0x58A364 + ([player] * 4 + [unitType] * 48)` is [AtLeast/AtMost/Exactly] [value].  
            Its synchronization depends on the synchronization of the data stored at `0x58A364 + ([player] * 4 + [unitType] * 48)`.  
            </details>
        - `DeathsX`(player: TrgPlayer, AtLeast/AtMost/Exactly: TrgComparison, value, unitType: TrgUnit, mask) : Condition  
            <details>

            <summary>This condition is usually not used to compare player unit deaths</summary>
        
            It is usually used to compare whether the 32-bit (unsigned integer value & [mask]) stored at `0x58A364 + ([player] * 4 + [unitType] * 48)` is [AtLeast/AtMost/Exactly] [value].  
            Its synchronization depends on the synchronization of the data stored at `0x58A364 + ([player] * 4 + [unitType] * 48)`.  
            
            </details>

        > **Note** 
        > Units killed or removed using trigger actions are not counted in the death count (Deaths);  
        > Suicidal units (Zerg Scourge, Infested Terran, Vulture Spider Mine) that successfully detonate are not counted in the death count (Deaths), but are counted if killed by other units (without successful detonation);  
        > Units killed by allies are also counted in the death count (Deaths).  
        
        Example

        ```JavaScript
        if ( Deaths(P1, AtLeast, 15, "Terran Marine") ) {
            // If player 1 has at least 15 Terran Marines deaths
        }
        ```

    <br />

    - #### **Memory**
        - `Memory`(memoryAddress, AtLeast/AtMost/Exactly : TrgComparison, value) : Condition  
            Compare whether the 32-bit unsigned integer stored at [memoryAddress] is [AtLeast/AtMost/Exactly] [value].  
            Its synchronization depends on the synchronization of the data stored at [memoryAddress].  

        - `MemoryX`(memoryAddress, AtLeast/AtMost/Exactly : TrgComparison, value, mask) : Condition  
            Compare whether the 32-bit (unsigned integer value & [mask]) stored at [memoryAddress] is [AtLeast/AtMost/Exactly] [value]  
            Its synchronization depends on the synchronization of the data stored at [memoryAddress].  

        - `MemoryEPD`(epd, AtLeast/AtMost/Exactly : TrgComparison, value) : Condition  
            Compare whether the 32-bit unsigned integer stored at `0x58A364 + ([epd] * 4)` is [AtLeast/AtMost/Exactly] [value]  
            Its synchronization depends on the synchronization of the data stored at `0x58A364 + ([epd] * 4)`.  

        - `MemoryXEPD`(epd, AtLeast/AtMost/Exactly : TrgComparison, value, mask) : Condition  
            Compare whether the 32-bit (unsigned integer value & [mask]) stored at `0x58A364 + ([epd] * 4)` is [AtLeast/AtMost/Exactly] [value]  
            Its synchronization depends on the synchronization of the data stored at `0x58A364 + ([epd] * 4)`.  

        Example

        ```JavaScript
        function MorphLarvaEPD(epd, newUnit: TrgUnit) {
            if (MemoryXEPD(epd + 0x64/4, Exactly, 35, 0xFFFF)) {
                SetMemoryXEPD(epd + 0x4D/4, SetTo, 42 << 8, 0xFFFF00);
                SetMemoryXEPD(epd + 0x98/4, SetTo, newUnit, 0xFFFF);
            }
        }
        ```

    <br />

    - #### **Kills**

        - `Kills`(player : TrgPlayer, AtLeast/AtMost/Exactly : TrgComparison, value, unitType : TrgUnit) : Condition  
            Compare whether the kills of [unitType] of [player] is [AtLeast/AtMost/Exactly] [value]  

            Kills is not kill score, note the difference  
            Killing own units is not counted in the Kills  
        
        Example

        ```JavaScript
        if ( Kills(P1, AtLeast, 15, "Terran Marine") ) {
            // If player 1 killed at least 15 Terran Marines
        }
        ```

    <br />

    - #### **ElapsedTime**

        - `ElapsedTime`(AtLeast/AtMost/Exactly : TrgComparison, game seconds) : Condition  
            Compare whether the elapsed game time is [AtLeast/AtMost/Exactly] [value] game seconds  

        This condition should not use Exactly to compare because trigger polling does not occur every game second. One game second is 16 game frames, not equal to one real second.  

        Example

        ```JavaScript
        if ( ElapsedTime(AtLeast, 5) ) {
            // The elapsed game time exceeds 5 game seconds
        }
        ```

    <br />

    - #### **LeastKills/MostKills**

        - `LeastKills`(unitType : TrgUnit) : Condition  
            Compare whether the `current player`'s kill count of [unitType] is the least on the map  

        - `MostKills`(unitType : TrgUnit) : Condition  
            Compare whether the `current player`'s kill count of [unitType] is the most on the map  

        Example

        ```JavaScript
         if (LeastKills("Terran Marine")) {  
            // The current player killed the least Terran Marines  
         }  

         if (MostKills("Terran Marine")) {  
            // The current player killed the most Terran Marines  
         }
        ```

    <br />

    - #### **LeastResources/MostResources**

        - `LeastResources`(resourceType : TrgResource) : Condition  
            Compare whether the `current player`'s [resourceType] is the least on the map

        - `MostResources`(resourceType : TrgResource) : Condition  
            Compare whether the `current player`'s [resourceType] is the most on the map

        Example

        ```JavaScript
        if ( LeastResources(Ore) ) {
            // The current player has the least ore
        }

        if ( MostResources(Gas) ) {
            // The current player has the most gas
        }
        ```

    <br />

    - #### **Opponents**

        - `Opponents`(player : TrgPlayer, AtLeast/AtMost/Exactly : TrgComparison, value) : Condition  
            Compare whether the number of opponents of [player] in the current game is [AtLeast/AtMost/Exactly] [value]  

        Example

        ```JavaScript
        if ( Opponents(P1, AtMost, 2) ) {
            // Player 1 has at most 2 opponents
        }
        ```

    <br />

    - #### **Score**

        - `Score`(player : TrgPlayer, score type : TrgScore, AtLeast/AtMost/Exactly : TrgComparison, value) : Condition  
            Compare whether the [score type] score of [player] is [AtLeast/AtMost/Exactly] [value] points  

        - `LowestScore`(score type : TrgScore) : Condition  
            Compare whether the current player's current [score type] is the lowest score  

        - `HighestScore`(score type : TrgScore) : Condition  
            Compare whether the current player's current [score type] is the highest score  

        Example

        ```JavaScript
         if (Score(P1, Kills, AtLeast, 10000)) {  
            // Player 1's kill score is at least 10000 points. Kill score is not kills, note the difference.  
         }  

         if (LowestScore(Buildings)) {  
            // If the current player's building score is now the lowest  
         }  

         if (HighestScore(Kills)) {  
            // If the current player's kill score is now the highest  
         }
        ```

    <br />

    - #### **Switch**

        - `Switch`(switch : TrgSwitch, state : TrgSwitchState) : Condition  
            Compare whether the state of [switch] is [state]  

        Example

        ```JavaScript
        if ( Switch($S("Switch 1"), Set) ) {
            // Switch 1 is Set
        }

        if ( Switch($S("Switch 1"), Cleared) ) {
            // Switch 1 is Cleared
        }
        ```

    <br />

    - #### **~~Always/Never~~**

        - ~~Always() : Condition~~  
            Always executes unconditionally, useless in epScript

        - ~~Never() : Condition~~  
            Never executes, In most cases, this function is useless in epScript.  

    <br />
    <br />

- ### Extended Condition Functions 


    - #### **IsUserCP**

        - `IsUserCP()`: Condition  
            Desync condition used to check if the local player is the current player  

    <br />

    - #### **Is64BitWireframe**

        - `Is64BitWireframe()`: Condition  
            Desync condition used to check if the local Starcraft client is 64-bit  


    <br />
    <br />

- ### Normal Action Functions

    Normal action functions are functions encapsulated based on classical triggers in ScmDraft 2.  
    Any trigger action function (including extended trigger functions) returns an action expression constant. The concepts of `action expression` and `executing action expression` need to be clearly distinguished.  
    If the non-comment code between two semicolons is only a call to an action function, epScript will pass it to an unconditional trigger DoActions for execution. Refer to the example:  

    ```JavaScript
    const a1 = CenterView($L("Location 1")); // This declares an action expression constant and does not execute it
    CenterView($L("Location 1")); // This means executing an action, equivalent to DoActions(CenterView($L("Location 1")));
    DoActions(a1); // The a1 declared in the first line is executed at this time
    ```

    <br />

    - #### **CenterView**

        - `CenterView`(location : TrgLocation) : Action  
            Allows desync execution and sets the `current player`'s camera to the [location]  

        Example

        ```JavaScript
        setcurpl(P1);
        CenterView($L("Location 1"));
        ```

    <br />

    - #### **CreateUnit**

        - `CreateUnit`(number, unitType : TrgUnit, location : TrgLocation, player : TrgPlayer) : Action  
            Create [number] of [unitType] for [player] at [location]. The moment a unit is created, the supply used by the unit will immediately (in the current frame) increase.  

        - `CreateUnitWithProperties`(number, unitType : TrgUnit, Where : location : TrgLocation, player : TrgPlayer, properties : TrgProperty) : Action  
            Create [number] of [unitType] with [properties] for [player] at [location]. The moment a unit is created, the supply used by the unit will immediately (in the current frame) increase.  

        Example

        ```JavaScript
        CreateUnit(2, "Terran Siege Tank", $L("Location 1"), P1);
        CreateUnitWithProperties(1, "Terran Marine", $L("Location 1"), P1, UnitProperty(
             hitpoint = 100,       // Health percentage  
             shield = 100,         // Shield percentage   
             energy = 100,         // Energy percentage  
             hanger = 0,           //  
             resource = 0,         //  
             cloaked = False,      // Whether invisible  
             burrowed = False,     // Whether burrowed 
             intransit = False,    // Whether being transported  
             hallucinated = False, // Whether hallucinated
             invincible = False)   // Whether invincible  
        );
        ```

    <br />

    - #### **Defeat/Victory/Draw**

        - `Defeat()` : Action  
            The current player loses and ends the game 

        - `Victory()` : Action  
            The current player wins and ends the game

        - `Draw()` : Action  
            All players draw and end the game

    <br />

    - #### **DisplayText**

        - `DisplayText`(text : TrgString) : Action  
            Allows desync execution and displays [text] on the next line of the text area on the current player's screen  

            > The argument [text] of this action is actually the number of this text entry in the map string table. If this entry does not exist in the map string table, epScript will first insert [text] into the map string table and then use its ID as its argument.   

        Example

        ```JavaScript
        const idx = $T("Hello StarCraft!");
        dbstr_print(GetMapStringAddr(idx), "WTF StarCraft!");
        DisplayText("Hello StarCraft!"); // Outputs WTF StarCraft!
        ```

    <br />

    - #### **GiveUnits**

        - `GiveUnits`(number : TrgCount, unitType : TrgUnit, owner : TrgPlayer, area : TrgLocation, recipient : TrgPlayer) : Action  
            Give up to [number] [unitType] units of [owner] player in [area] to [recipient] player. [number] = 0 represents all units.  

            > This action will cause the rally points of the given units to be lost.  

        Example

        ```JavaScript
        // Give up to 3 Marines of Player 2 in Location 1 to Player 1
        GiveUnits(3, "Terran Marine", P2, $L("Location 1"), P1);
        ```

    <br />

    - #### **KillUnit**

        - `KillUnit`(unitType : TrgUnit, player : TrgPlayer) : Action  
            Kill all [unitType] units of [player], including units still in the build queue and nuclear missiles not yet launched in nuclear silos.  

        - `KillUnitAt`(number : TrgCount, unitType : TrgUnit, specified area : TrgLocation, player : TrgPlayer) : Action  
            Kill up to [number] [unitType] units of [player] in [specified area]. [number] = 0 represents all units. Does not include units still in the build queue or nuclear missiles not yet launched in nuclear silos.  

            > KillUnitAt(All, "Scanner Sweep", "Anywhere", P1) cannot kill Scanner Sweeps.  
            > KillUnitAt(All, "Map Revealer", "Anywhere", P1) cannot kill Map Revealers.  

            > **Warning**  
            > This action has a bug:  
            > If this action kills any unit inside a transporter (Dropship/Bunker, etc.), then all units of the same type inside that transporter (Dropship/Bunker, etc.) will be killed, and these killed units will not be counted within the [number] parameter specified.  
            > For example, if executing KillUnitAt(1, "Terran Marine", "Location 1", P1) kills a marine inside a bunker in Location 1, then all marines in that bunker will be killed, and if there are more marines outside the bunker in that area, one more will be killed.  

        Example

        ```JavaScript
        KillUnit("Terran Marine", P1); // Kill all Marines of Player 1
        KillUnitAt(3, "Terran Siege Tank", $L("Location 1"), P1) // Kill up to 3 Tanks of Player 1 in Location 1
        ```

    <br />

    - #### **LeaderBoard**

        - `LeaderBoardComputerPlayers`(state : TrgPropState) : Action  
            Set the enabled state of the LeaderBoard for computer players.  

        - `LeaderBoardControl`(unitType : TrgUnit, label : TrgString) : Action  
            Display a LeaderBoard in descending order of all players' [unitType] control counts described as [label].  

        - `LeaderBoardControlAt`(unitType : TrgUnit, area : TrgLocation, label : TrgString) : Action  
           Display a LeaderBoard in descending order of all players' [unitType] control counts in [area] described as [label].  

        - `LeaderBoardGoalControl`(goal, unitType : TrgUnit, label : TrgString) : Action  
            Display a LeaderBoard in descending order of all players' [unitType] control counts closest to [goal] described as [label].  

        - `LeaderBoardGoalControlAt`(goal, unitType : TrgUnit, area : TrgLocation, label : TrgString) : Action  
            Display a LeaderBoard in descending order of all players' [unitType] control counts in [area] closest to [goal] described as [label].  

        - `LeaderBoardGoalKills`(goal, unitType : TrgUnit, label : TrgString) : Action  
            Display a LeaderBoard in descending order of all players' kills of [unitType] closest to [goal] described as [label].  

        - `LeaderBoardGoalResources`(goal, resourceType : TrgResource, label : TrgString) : Action  
            Display a LeaderBoard in descending order of all players' collections of [resourceType] closest to [goal] described as [label].  

        - `LeaderBoardGoalScore`(goal, scoreType : TrgScore, label : TrgString) : Action  
            Display a LeaderBoard in descending order of all players' [scoreType] scores closest to [goal] described as [label].  

        - `LeaderBoardGreed`(goal) : Action  
            Display a LeaderBoard in descending order of all players' collections of crystal and gas mines closest to [goal].  

        - `LeaderBoardKills`(unitType : TrgUnit, label : TrgString) : Action  
            Display a LeaderBoard in descending order of all players' kills of [unitType] described as [label].  

        - `LeaderBoardResources`(resourceType : TrgResource, label : TrgString) : Action  
            Display a LeaderBoard in descending order of all players' collections of [resourceType] described as [label].  

        - `LeaderBoardScore`(scoreType : TrgScore, label : TrgString) : Action  
            Display a LeaderBoard in descending order of all players' [scoreType] scores described as [label].  

        Example

        ```JavaScript
        LeaderBoardGoalControlAt(10, "Terran Marine", $L("Destination"), "Marines reaching destination");
        ```

    <br />

    - #### **MinimapPing**

        - `MinimapPing`(location : TrgLocation) : Action  
            Allow desync execution. Display a Ping on the minimap at [specified location] for the current player.  

        Example

        ```JavaScript
        // Display Ping at Location 1 on Minimap for Player 1
        setcurpl(P1);
        MinimapPing($("Location 1"));
        ```

    <br />

    - #### **ModifyUnit**

        - `ModifyUnitEnergy`(number : TrgCount, unitType : TrgUnit, player : TrgPlayer, area : TrgLocation, percentage) : Action  
            Change the energy of up to [number] [unitType] units of [player] in [area] to [percentage] percent. [number] = 0 represents all (All) units.  

        - `ModifyUnitHangarCount`(added, number : TrgCount, unitType : TrgUnit, player : TrgPlayer, area : TrgLocation) : Action  
            Add up to [added] loaded units to up to [number] [unitType] units of [player] in [area]. [number] = 0 represents all (All) units.  

            For example, Interceptors in Carriers, Scarabs in Reavers. Note that this action cannot add Spider Mines to Vultures.  

        - `ModifyUnitHitPoints`(number : TrgCount, unitType : TrgUnit, player : TrgPlayer, area : TrgLocation, percentage) : Action  
            Change the hit points of up to [number] [unitType] units of [player] in [area] to [percentage] percent. [number] = 0 represents all (All) units.  

        - `ModifyUnitResourceAmount`(number : TrgCount, player : TrgPlayer, area : TrgLocation, new value) : Action  
            Change the resource value of up to [number] units of [player] in [area] to [new value]. [number] = 0 represents all (All) units.  

        - `ModifyUnitShields`(number : TrgCount, unitType : TrgUnit, player : TrgPlayer, area : TrgLocation, percentage) : Action  
            Change the shields of up to [number] [unitType] units of [player] in [area] to [percentage] percent. [number] = 0 represents all (All) units.  

        Example

        ```JavaScript
        // Change the hit points of up to 100 Marines of Player 1 in Location 1 to 100%
        ModifyUnitHitPoints(100, "Terran Marine", P1, $L("Location 1"), 100);
        ```

    <br />

    - #### **MoveLocation**

        - `MoveLocation`(location : TrgLocation, unitType : TrgUnit, player : TrgPlayer, area : TrgLocation) : Action  
            Move the center of [location] onto one of the [unitType] units of [player] in [area].  

        Example

        ```JavaScript
        // Move the center of Location 1 onto one of Player 1's Marines anywhere on the map
        MoveLocation($L("Location 1"), "Terran Marine", P1, $L("AnyWhere"));
        ```

    <br />

    - #### **MoveUnit**

        - `MoveUnit`(number : TrgCount, unitType : TrgUnit, player : TrgPlayer, startArea : TrgLocation, targetLocation : TrgLocation) : Action  
            Instantly move up to [number] [unitType] units of [player] in [startArea] to [targetLocation]. [number] = 0 represents all (All) units.  

        Example

        ```JavaScript
        // Instantly move up to 10 Marines of Player 1 in Location 1 to Location 2
        MoveUnit(10, "Terran Marine", P1, $L("Location 1"), $L("Location 2"));
        ```

    <br />

    - #### **MuteUnitSpeech/UnMuteUnitSpeech**

        - `MuteUnitSpeech()` : Action  
            Allow desynchronized execution. Mute all speeches of the current player's units (except trigger units' speeches).  

        - `UnMuteUnitSpeech()` : Action  
            Allow desynchronized execution. Unmute all speeches of the current player's units (except trigger units' speeches).  

    <br />

    - #### **Order**

        - `Order`(unitType : TrgUnit, player : TrgPlayer, startArea : TrgLocation, order : TrgOrder, targetLocation : TrgLocation) : Action  
            Issue an [order] for [player]'s [unitType] units in [startArea] towards the center of [targetLocation].  

        Example

        ```JavaScript
        // Order all Marines of Player 1 in Location 1 to attack-move to the center of Location 2
        Order("Terran Marine", P1, $L("Location 1"), Attack, $L("Location 2"))
        ```

    <br />

    - #### **PauseGame/UnpauseGame**

        - `PauseGame()` : Action  
            Pause the game for all players.  

        - `UnpauseGame()` : Action  
            Unpause the game for all players.  

    <br />

    - #### **PauseTimer/UnpauseTimer**

        - `PauseTimer()` : Action  
            Pause the countdown timer for all players.  

        - `UnpauseTimer()` : Action  
            Unpause the countdown timer for all players.  

    <br />

    - #### **PlayWAV**

        - `PlayWAV`(WAVName : TrgString) : Action  
            Allow desynchronized execution. Play a WAV file named [WAVName] for the current player.

    <br />

    - #### **~~PreserveTrigger~~**

        - ~~PreserveTrigger() : Action~~  
            Preserve the trigger. Because classical triggers become disabled after executing once, this action is needed to repeatedly trigger. Useless in epScript.

    <br />

    - #### **RemoveUnit**

        - `RemoveUnit`(unitType : TrgUnit, player : TrgPlayer) : Action  
            Remove all [unitType] units of [player] from the map, including units still in the production queue. Can remove nuclear missiles that have not been launched in Nuclear Silos. The supply used by the removed units will decrease in the next frame.  

        - `RemoveUnitAt`(number : TrgCount, unitType : TrgUnit, area : TrgLocation, player : TrgPlayer) : Action  
            Remove up to [number] [unitType] units of [player] in [area] from the map, [number] = 0 represents all (All) units. Does not include units still in the production queue. Will not remove nuclear missiles that have not been launched in Nuclear Silos. The supply used by the removed units will decrease in the next frame.  

            > RemoveUnitAt(All, "Scanner Sweep", "Anywhere", P1) cannot remove Scanner Sweeps.   
            > RemoveUnitAt(All, "Map Revealer", "Anywhere", P1) cannot remove Map Revealers.  

            > **Warning**  
            > This action has a bug:  
            > If this action removes any unit inside a transporter (Dropship/Bunker, etc.), then all units of the same type inside that transporter (Dropship/Bunker, etc.) will be removed, and these removed units will not be counted within the [number] parameter specified.  
            > For example, if executing RemoveUnitAt(1, "Terran Marine", "Location 1", P1) removes a marine inside a bunker in Location 1, then all marines in that bunker will be removed, and if there are more marines outside the bunker in that area, one more will be removed.  

    <br />

    - #### **RunAIScript**

      - `RunAIScript`(Script : TrgAIScript) : Action  
            Run AI script [Script] for the current player.  

      - `RunAIScriptAt`(Script : TrgAIScript, area : TrgLocation) : Action  
            Run AI script [Script] for the current player in [area].  
        
        Example

        ```JavaScript
        RunAIScriptAt("Terran Custom Level", $L("Location 1"));
        ```

    <br />

    - #### **SetAllianceStatus**

      - `SetAllianceStatus`(targetPlayer : TrgPlayer, status : TrgAllyStatus) : Action  
            Set the alliance status of the current player towards [targetPlayer] to [status].  

        Example

        ```JavaScript
        // Set Player 1 allied towards Player 2, Player 2 enemy towards Player 1
        setcurpl(P1);
        SetAllianceStatus(P2, Ally);
        setcurpl(P2);
        SetAllianceStatus(P1, Enemy);
        ```

    <br />

    - #### **SetCountdownTimer**

      - `SetCountdownTimer`(SetTo/Add/Subtract : TrgModifier, number) : Action  
            Set countdown timer to [SetTo/Add/Subtract] [number] game seconds. 1 game second = 16 frames.  
        
        Example

        ```JavaScript
        SetCountdownTimer(SetTo, 100); // Set countdown timer to 100 game seconds  
        SetCountdownTimer(Add, 5); // Add 5 game seconds to countdown timer       
        SetCountdownTimer(Subtract, 3); // Subtract 3 game seconds from countdown timer 
        ```

    <br />

    - #### **SetDeaths**

        - `SetDeaths`(player : TrgPlayer, SetTo/Add/Subtract : TrgModifier, value, unitType : TrgUnit) : Action  
            Set the number of deaths of [player]'s [unitType] units to [SetTo/Add/Subtract] [value].  

            <details>

            <summary>When [player] or [unitType] is out of range</summary> 

            It will be an EUD action to set the current value stored at memory address `0x58A364 + ([player] * 4 + [unitType] * 48)` to [SetTo/Add/Subtract] [value].  
            Whether desynchronized execution is allowed depends on the synchronicity of the data stored at memory address `0x58A364 + ([player] * 4 + [unitType] * 48)`. 
            </details> 

      - `SetDeathsX`(player : TrgPlayer, SetTo/Add/Subtract: TrgModifier, value, unitType: TrgUnit, mask) : Action  
        <details>

        <summary>This function is not usually used to set player unit death counts.</summary>

        ```Markdown
         SetTo   : Set the current value stored at memory address `0x58A364 + ([player] * 4 + [unitType] * 48)` to `current value - (current value & mask) + (value & mask)`  
         Add     : Set the current value stored at memory address `0x58A364 + ([player] * 4 + [unitType] * 48)` to `current value - (current value & mask) + ( ((current value & mask) + (value & mask)) & mask )`  
         Subtract: Set the current value stored at memory address `0x58A364 + ([player] * 4 + [unitType] * 48)` to `current value - (current value & mask) + ( ((current value & mask) - (value & mask)) & mask )` (the subtraction in the formula can subtract to a minimum of 0)  
        ```
        Whether desynchronized execution is allowed depends on the synchronicity of the data stored at memory address `0x58A364 + ([player] * 4 + [unitType] * 48)`  
        </details>


        Example

        ```JavaScript
        SetDeaths(P1, Add, 10, "Terran Marine"); // Add 10 to the number of deaths of Player 1's Marines
        ```

    <br />

    - #### **SetMemory**

        - `SetMemory`(memoryAddress, SetTo/Add/Subtract : TrgModifier, value) : Action  
            Set the 32-bit positive integer value stored at [memoryAddress] to [SetTo/Add/Subtract] [value].  
            Whether desynchronized execution is allowed depends on the synchronicity of the data stored at [memoryAddress].  

        - `SetMemoryX`(memoryAddress, SetTo/Add/Subtract : TrgModifier, value, mask) : Action  
            <details>

            <summary>SetMemory that supports mask access, can modify any one or more bits of 32 bits.</summary>

            ```Markdown
            SetTo   : Set the current value stored at [memoryAddress] to `current value - (current value & mask) + (value & mask)`  
            Add     : Set the current value stored at [memoryAddress] to `current value - (current value & mask) + ( ((current value & mask) + (value & mask)) & mask )`  
            Subtract: Set the current value stored at [memoryAddress] to `current value - (current value & mask) + ( ((current value & mask) - (value & mask)) & mask )` (the subtraction in the formula can subtract to a minimum of 0)  
            ```
           Whether desynchronized execution is allowed depends on the synchronicity of the data stored at [memoryAddress].  
            </details>


        - `SetMemoryEPD`(epd : TrgPlayer, SetTo/Add/Subtract : TrgModifier, value) : Action  
            Set the 32-bit positive integer value stored at memory address `0x58A364 + ([epd] * 4)` to [SetTo/Add/Subtract] [value].  
            Whether desynchronized execution is allowed depends on the synchronicity of the data stored at memory address `0x58A364 + ([epd] * 4)`. 

        - `SetMemoryXEPD`(epd : TrgPlayer, SetTo/Add/Subtract : TrgModifier, value, mask) : Action  
            <details>

            <summary>SetMemoryEPD that supports mask access, can modify any one or more bits of 32 bits.</summary>

            ```Markdown
            SetTo   : Set the current value stored at memory address `0x58A364 + ([epd] * 4)` to `current value - (current value & mask) + (value & mask)`  
            Add     : Set the current value stored at memory address `0x58A364 + ([epd] * 4)` to `current value - (current value & mask) + ( ((current value & mask) + (value & mask)) & mask )`  
            Subtract: Set the current value stored at memory address `0x58A364 + ([epd] * 4)` to `current value - (current value & mask) + ( ((current value & mask) - (value & mask)) & mask )` (the subtraction in the formula can subtract to a minimum of 0)  
            ```
            Whether desynchronized execution is allowed depends on the synchronicity of the data stored at memory address `0x58A364 + ([epd] * 4)`.  
            </details>

        Example
        ```JavaScript
        function MorphLarvaEPD(epd, newUnit: TrgUnit) {
            if (MemoryXEPD(epd + 0x64/4, Exactly, 35, 0xFFFF)) {
                SetMemoryXEPD(epd + 0x4D/4, SetTo, 42 << 8, 0xFFFF00);
                SetMemoryXEPD(epd + 0x98/4, SetTo, newUnit, 0xFFFF);
            }
        }
        ```

    <br />

    - #### **SetDoodadState**

        - `SetDoodadState`(state : TrgPropState, unitType : TrgUnit, player : TrgPlayer, area : TrgLocation) : Action  
            Set the Doodad state of [player]'s [unitType] units in [area] to [state].  

        Example

        ```JavaScript
        SetDoodadState(Enable, "Terran Marine", P1, $L("Location 1"));
        ```

    <br />

    - #### **SetInvincibility**

        - `SetInvincibility`(state : TrgPropState, unitType : TrgUnit, player : TrgPlayer, area : TrgLocation) : Action  
            Set the invincibility state of [player]'s [unitType] units in [area] to [state].  

        Example

        ```JavaScript
        SetInvincibility(Enable, "Terran Marine", P1, $L("Location 1")); // Set the invincibility state of Player 1's Marines in Location 1 to Enable
        SetInvincibility(Disable, "Terran Marine", P1, $L("Location 1")); // Set the invincibility state of Player 1's Marines in Location 1 to Disable
        ```

    <br />

    - #### **SetMissionObjectives**

        - `SetMissionObjectives`(text : TrgString) : Action  
             Allows desynchronized execution. Set the current player's mission objectives description to [text].   

            > The argument [text] of this action is actually the ID of this text entry in the Map String Table. If this entry does not exist in the Map String Table, epScript will first insert this [text] into the Map String Table and then use its ID as the argument.  

        Example

        ```JavaScript
        SetMissionObjectives("Our objectives are:\nNo cavities!");
        ```

    <br />

    - #### **~~SetNextScenario~~**

        - ~~`SetNextScenario`(text : TrgString) : Action~~  
            Set the name of the next map to load after the current game ends to [text]. Must be in the same directory.   

            > **Note**
            > `SetNextScenario` is singleplayer-only and currently does not work on EUD maps (useless at the moment).


    <br />

    - #### **SetResources**

        - `SetResources`(player : TrgPlayer, SetTo/Add/Subtract : TrgModifier, value, resourceType : TrgResource) : Action  
         Set [player]'s [resourceType] resources to [SetTo/Add/Subtract] [value].  

        Example

        ```JavaScript
        SetResources(P1, Add, 1000, Ore); // Give Player 1 1000 Ore
        SetResources(P1, Substract, 1000, Gas); // Take 1000 Gas from Player 1
        SetResources(P1, SetTo, 5000, OreAndGas); // Set Player 1's Ore and Gas resources to 5000
        ```

    <br />

    - #### **SetScore**

        - `SetScore`(player : TrgPlayer, SetTo/Add/Subtract : TrgModifier, value, scoreType : TrgScore) : Action  
            Set [player]'s [scoreType] score to [SetTo/Add/Subtract] [value].  

        Example

        ```JavaScript
        SetScore(P1, Add, 1000, Kills); // Give Player 1 1000 Kills score
        ```

    <br />

    - #### **SetSwitch**

        - `SetSwitch`(switchName : TrgSwitch, switchAction : TrgSwitchAction) : Action  
            Set the state of switch [switchName] to [switchAction].  

        Example

        ```JavaScript
        SetSwitch($S("Switch 1"), Set);    // Set Switch 1 state to Set
        SetSwitch($S("Switch 1"), Clear);  // Set Switch 1 state to Cleared
        SetSwitch($S("Switch 1"), Toggle); // Toggle Switch 1 state, if it was originally Set it will be switched to Cleared, if it was originally Cleared it will be switched to Set
        SetSwitch($S("Switch 1"), Random); // Set Switch 1 to a random state, after using it Switch 1's state may be Set or may be Cleared
        ```

    <br />

    - #### **TalkingPortrait**

        - `TalkingPortrait`(unitType : TrgUnit, milliseconds) : Action  
            Allows desynchronized execution. Display the portrait of [unitType] at the current player's unit portrait for [milliseconds] game milliseconds.  

        Example

        ```JavaScript
        // Have the Marine give instructions to Player 1
        setcurpl(P1);
        TalkingPortrait("Terran Marine", 5000);
        ```

    <br />

    - #### **Transmission**

        - ~~`Transmission`(unitType : TrgUnit, area : TrgLocation, WAVName : TrgString, SetTo/Add/Subtract : TrgModifier, time, text : TrgString) : Action~~  
            Allows desynchronized execution. Play a sound [WAVName] for the current player and display the portrait of [unitType] units in [area] at the player's unit portrait for [SetTo/Add/Subtract] [time] game milliseconds, while pinging the unit on the minimap and outputting the text information [text].  

            > **Note**
            > This function will affect trigger control flow, it is not recommended to use in epScript.

        Example

        ```JavaScript
        Transmission("Terran Marine", $L("Location 3"), "sound\\Zerg\\Advisor\\ZAdUpd00.WAV", Add, 5000, "Our objectives are:\nNo cavities!");
        ```

    <br />

    - #### **~~Wait~~**

        - ~~Wait(milliseconds) : Action~~

            > **Note**
            > This function will affect trigger control flow, it is not recommended to use in epScript.


    <br />
    <br />


- ### Extended Action Functions

    Extended action functions are functions that cannot be found in classical triggers but can still be regarded as trigger actions. They will return action constant expressions or expression lists. 
    They can be added to RawTrigger or DoActions action lists, and may no longer be a single trigger action.   

    <br />

    - #### **SetKills**

        - `SetKills`(player : TrgPlayer, SetTo/Add/Subtract : TrgModifier, value, unitType : TrgUnit) : Action | [Action]  
            Set [player]'s kills against [unitType] to [SetTo/Add/Subtract] [value].  
            Kills are not kill scores, note the difference.  
            Composed of one or three classical trigger actions, depending on whether the player number is CurrentPlayer.  

        Example

        ```JavaScript
        // https://armoha.github.io/eud-book/offsets/KilledUnitCountsTable.html  
        // In fact, there is no SetKills action in classical triggers, it is simulated by EUD.  

        // If the player number is not CurrentPlayer (13), its internal implementation is probably like this, returning a constant expression  
        SetDeaths(player number - 2736, SetTo/Add/Subtract, value, unitType);  

        // If the player number is CurrentPlayer (13), its internal implementation is probably like this, returning a tuple containing three constant expressions  
        DoActions(  
             SetDeaths(EPD(0x6509B0), Add, -2736, 0),  
             SetDeaths(CurrentPlayer, SetTo/Add/Subtract, value, unitType),  
             SetDeaths(EPD(0x6509B0), Add, 2736, 0),  
         ); 
        ```

    <br />

    - #### **SetCurrentPlayer**

        - `SetCurrentPlayer`(playerID : TrgPlayer) : [Action]  
            Allows desynchronized execution. Set `CurrentPlayer` and cpcache to [playerID].  
            Composed of three classical trigger actions.  

        Example

        ```JavaScript
        RawTrigger(actions = list(
            SetCurrentPlayer(P1),
            DisplayText("Content displayed to Player 1"),
            SetCurrentPlayer(P2),
            DisplayText("Content displayed to Player 2"),
            SetCurrentPlayer(P3),
            DisplayText("Content displayed to Player 3"),
        ));
        ```

    <br />

    - #### **AddCurrentPlayer**

        - `AddCurrentPlayer`(playerid : TrgPlayer) : [Action]  
            Allows desynchronized execution. Set `CurrentPlayer` and cpcache to [playerID].  
            Composed of three classical trigger actions.  

        Example

        ```JavaScript
        RawTrigger(actions = list(
            SetCurrentPlayer(P3),
            DisplayText("Content displayed to Player 3"),
            AddCurrentPlayer(-1),
            DisplayText("Content displayed to Player 2"),
            AddCurrentPlayer(-1),
            DisplayText("Content displayed to Player 1"),
        ));

        // https://armoha.github.io/eud-book/offsets/GameSpeedRefreshRate.html
        // Set all game speeds from Slowest to Fastest to 200%
        RawTrigger(actions = list(
            SetCurrentPlayer(EPD(0x5124D8)),
            SetDeaths(CurrentPlayer, SetTo, 21, 0),
            AddCurrentPlayer(1),
            SetDeaths(CurrentPlayer, SetTo, 21, 0),
            AddCurrentPlayer(1),
            SetDeaths(CurrentPlayer, SetTo, 21, 0),
            AddCurrentPlayer(1),
            SetDeaths(CurrentPlayer, SetTo, 21, 0),
            AddCurrentPlayer(1),
            SetDeaths(CurrentPlayer, SetTo, 21, 0),
            AddCurrentPlayer(1),
            SetDeaths(CurrentPlayer, SetTo, 21, 0),
            AddCurrentPlayer(1),
            SetDeaths(CurrentPlayer, SetTo, 21, 0),
        ));
        ```

    <br />

    - #### **DisplayTextAll**

        - `DisplayTextAll`(text : TrgString) : [Action]  
            Display [text] on the next line of the text area for all players (including observers).  
            Composed of two classical trigger actions.

    <br />

    - #### **PlayWAVAll**

        - `PlayWAVAll`(WAVName) : [Action]  
            Play the sound [WAVName] for all players (including observers).  
            Composed of two classical trigger actions.  

    <br />

    - #### **MinimapPingAll**

        - `MinimapPingAll`(location) : [Action]  
            Issue a ping at [location] on the minimap for all players (including observers).  
            Composed of two classical trigger actions.  

    <br />

    - #### **CenterViewAll**

        - `CenterViewAll`(location) : [Action]  
            Center the camera on [location] for all players (including observers).  
            Composed of two classical trigger actions.  

    <br />

    - #### **SetMissionObjectivesAll**

        - `SetMissionObjectivesAll`(text : TrgString) : [Action]  
            Set the mission objectives text to [text] for all players (including observers).  
            Composed of two classical trigger actions.  

    <br />

    - #### **TalkingPortraitAll**

        - `TalkingPortraitAll`(unitType, milliseconds) : [Action]  
            Display the portrait of [unitType] at all players' (including observers) unit portraits for [milliseconds] game milliseconds.  
            Composed of two classical trigger actions.  

    <br />

    - #### **SetNextPtr**

        - `SetNextPtr`(trg, dest) : Action  
            Set the next trigger pointer of trigger [trg] to [dest].  
            It is essentially a SetDeaths action `SetDeaths(EPD(trg + 4), SetTo, dest, 0)`  

        Example

        ```javascript
        // The .getDestAddr() method of a variable can obtain the destination address in the variable trigger at compile time.
        // The .getValueAddr() method of a variable can obtain the value address in the variable trigger at compile time. 
        // The .GetVTable() method of a variable can obtain the virtual trigger address of the variable at compile time.
        // The .SetModifier(method) method of a variable sets the numeric modification method of the variable trigger to method.
        // The SetNextPtr(trg, ptr) function is used to set the next trigger of trg to ptr.
        function afterTriggerExec() {  
            var a, b = 3, 5;  
            const next = Forward();  
            RawTrigger(  
                actions = list(  
                    SetMemory(b.getValueAddr(), Add, 1),  
                    SetMemory(a.getValueAddr(), Add, 1),  
                    SetMemory(b.getDestAddr(), SetTo, EPD(a.getValueAddr())),  
                    b.SetModifier(Add), // Internally it is probably implemented as SetMemoryX(b.getValueAddr() + 4, SetTo, (Add << 24), 0xFF000000)  
                    SetNextPtr(b.GetVTable(), next), // Set the next trigger of b to next, the internal implementation may be like this: SetMemory(b.GetVTable() + 4, SetTo, next)  
                ),  
                nextptr = b.GetVTable(), // The next trigger of this trigger is b  
            );  
            next.__lshift__(NextTrigger()); // The essence of this is to point next, the Forward, to the next Trigger  
            // The result is a:10 b:6  
        }
        ```


    <br />
    <br />
    <br />

## Extended Functions  
- ### Compile Time

    - #### **Get Index**

        - `$L`(areaName : literal) : py_int  
        - `GetLocationIndex`(areaName : py_str) : py_int  
        - `EncodeLocation`(areaName : py_str) : py_int  
            Gets the [areaName] defined in the map editor (usually SCMD) converted to the corresponding area ID. All functions with TrgLocation type parameters will automatically use this macro.  

        - `$T`(text : literal) : py_int  
        - `GetStringIndex`(text : py_str) : py_int  
        - `EncodeString`(text : py_str) : py_int  
            Gets the ID of an [text] entry in the map string table (Map String Table). All functions with TrgString type parameters will automatically use this macro, that is, functions that accept TrgString type parameters actually accept the ID of the string entry in the map string table.  

            > This macro can arbitrarily provide [text] keys. If the map string table already contains the [text] entry, the ID of the entry in the map string table is returned. If the map string does not have a [text] entry, a new ID→text key-value pair is inserted into the map string table and the ID is returned.

            > For example, $T("Force 1") will return 4 because it already exists. And $T("\x03Pool farmer") may return 3 (and at the same time create a new item 3: "\x03Pool farmer" in the map string dictionary).  

        - `$S`(switchName : literal) : py_int  
        - `GetSwitchIndex`(switchName : py_str) : py_int  
        - `EncodeSwitch`(switchName : py_str) : py_int  
            Gets the [switchName] defined in the map editor (usually SCMD) converted to the corresponding switch ID. All functions with TrgSwitch type parameters will automatically use this macro.  

        - `$U`(unitType : literal) : py_int  
        - `GetUnitIndex`(unitType : py_str) : py_int  
        - `EncodeUnit`(unitType : py_str) : py_int  
            Gets the [unitType] in the map unit.dat converted to the corresponding unitTypeID. All functions with TrgUnit type parameters will automatically use this macro.  

        - `$B`(TBLKey : literal) : py_int  
        - `EncodeTBL`(TBLKey : py_str) : py_int  
            Gets the index ID corresponding to [TBLKey] in the map TBL dictionary. All functions with StatText type parameters will automatically use this macro.  

        - `EncodeWeapon`(weaponName : py_str) : py_int  
            Gets the [weaponName] in the map weapon.dat converted to the corresponding weapon name ID. All functions with Weapon type parameters will automatically use this macro.  

        - `EncodeTech`(techName : py_str) : py_int  
            Gets the [techName] in the map tech.dat converted to the corresponding technology name ID. All functions with Tech type parameters will automatically use this macro.  

        All $ syntax macros ($L, $T, $S, $U, $B) only support literal strings as parameters.  

        Example

        ```PHP
        const l1 = $L("Location 1");
        const s2 = $S("Switch 2");
        const ut = $U("Terran Marine"); // Returns 0
        const aiid = $B("AI Harass Here"); // Returns 1538

        // Change the string ID of the SCV unit name. $T("\x03Pool farmer") will insert a new string into the map during compilation and return the ID of this string here.
        // https://armoha.github.io/eud-book/offsets/Units.dat-MapString.html
        wwrite(0x660260 + 2 * $U("Terran SCV"), $T("\x03Pool farmer"));

        // You can directly use $ syntax constants 
        // EncodePlayer 
        if (EncodePlayer(P1) == $P1) { py_print($P1, $P2, $CurrentPlayer, $AllPlayers, $Force1, $NonAlliedVictoryPlayers); } 
        // EncodeModifier 
        if (EncodeModifier(SetTo) == $SetTo) { py_print($SetTo, $Add, $Subtract); }
        // EncodeComparison 
        if (EncodeComparison(AtLeast) == $AtLeast) { py_print($Exactly, $AtLeast, $AtMost); } 
        // EncodeResource
        if (EncodeResource(OreAndGas) == $OreAndGas) { py_print($Ore, $Gas, $OreAndGas); }
        // EncodeSwitchAction 
        if (EncodeSwitchAction(Set) == $Set) { py_print($Set, $Clear, $Toggle, $Random); } // $Set == EncodeSwitchAction(Set)  
        // EncodeSwitchState
        if (EncodeSwitchState(Set) != $Set) { py_print($Cleared); } // Note this!!! $Set != EncodeSwitchState(Set)    
        // EncodeAllyStatus 
        if (EncodeAllyStatus(Ally) == $Ally) { py_print($Enemy, $Ally, $AlliedVictory); }   
        // EncodeOrder 
        if (EncodeOrder(Move) == $Move) { py_print($Move, $Patrol, $Attack); }   
        // EncodePropState
        if (EncodePropState(Enable) == $Enable) { py_print($Enable, $Disable, $Toggle); }
        // EncodeScore 
        if (EncodeScore(Total) == $Total) { py_print($Total, $Units, $Buildings, $UnitsAndBuildings, $Razings, $KillsAndRazings, $Custom); } // There is no $Kills, EncodeScore(Kills) == 4 
        // EncodeCount
        if (EncodeCount(All) == 0) { py_print(EncodeCount(All)); } // EncodeCount(All) is 0, EncodeCount any positive integer is equal to that positive integer itself  

        // Some less commonly used ones, I didn't write the documentation and examples, the usage is consistent, refer to the constants reference
        // EncodeAIScript
        // EncodeFlingy
        // EncodeIcon
        // EncodeImage
        // EncodeIscript
        // EncodePortrait
        // EncodeProperty
        // EncodeSprite
        // EncodeUnitOrder
        // EncodeUpgrade
        ```

    <br />

    - #### **list**

        - `list`(*args) : py_list  
            Creates and returns a flat compile-time Python list. It requires at least one argument. This function will automatically flatten lists and cannot create multi-dimensional lists.  
            If you want to create an empty compile-time list, use the py_list function.  
            Compile-time lists can be iterated at compile time using foreach syntax, and their indices can only be constants.  

        Example

        ```JavaScript
        var a, b, c, d;  
        const list1 = list(a, b, c, d); // list is a compile-time container, it just references a/b/c/d here, not the values of a/b/c/d
        const list2 = list(15, 4, list(99, 47)); // The list will be flattened, no multi-dimensional list will be created, this is equivalent to list(15, 4, 99, 47)
        foreach(i, v : py_enumerate(list2)) {
            list1[i] = v;  
        }
        println("{}, {}, {}, {}", a, b, c, d); // 15, 4, 99, 47
        ```

    <br />

    - #### **EUDCreateVariables**

        - `EUDCreateVariables`(count) : py_list[EUDVariable]  
            Creates [count] variables at compile time and returns a compile-time list containing references to the created variables.   
            Compile-time lists can be iterated at compile time using foreach syntax, and their indices can only be constants.  

        Example

        ```JavaScript
        const vs = EUDCreateVariables(3);
        vs[0] = 1;
        vs[1] = 2;
        vs[2] = 3;
        // vs[0], vs[1], and vs[2] are three variables. vs does not exist at runtime, so the index of vs must be a compile-time constant.
        ```

    <br />

    - #### **SetVariables**

        - `SetVariables`(varList : py_list, number : py_list, opList : py_list)  
            Uses at least one trigger to set all variables in [varList] to [number] values according to the corresponding operators in [opList]. This macro is used to optimize.  
            Even if the target value is a variable, it will not take effect dynamically before the action is completed. It will only keep the target value as the state when it started executing.  

        Example

        ```JavaScript
        var a, b, c = 10, 10, 10;
        SetVariables(
        list(  a,    b,      c   ),
        list(  3,    2,      4   ),
        list(SetTo, Add, Subtract),
        );
        // The above code is equivalent to
        const op1 = list(a,    SetTo, 3),
                    list(b,      Add, 2),
                    list(c, Subtract, 4);
        SeqCompute(op1);
        ```

    <br />

    - #### **SCMD2Text**

        - `SCMD2Text`(text) : py_str  
            Compile-time converts the hexadecimal numeric values \<XX\> in the text [text] to the corresponding ASCII characters.  

        Example

        ```JavaScript
        // The following two lines are equivalent
        simpleprint(SCMD2Text("<03>Haha<02>")); // Print yellow Haha
        simpleprint("\x03Haha\x02"); // Print yellow Haha
        ```

    <br />

    - #### **unProxy**

        - `unProxy`(x) : duck  
            Compile-time gets the pointer value of the reference type x.  

        Example

        ```JavaScript
        const a = EUDArray(list(9, 8, 7));
        var b = unProxy(a);
        const c = EUDArray.cast(b + 4); // c is actually a reference to a[1]
        c[0] = 888888;
        println("b:{} a:{} c:{} a[1]:{} c[0]:{}", b, a, c, a[1], c[1]); // b:421156492 a:421156492 c:421156496 a[1]:888888 c[1]:7
        ```

    <br />

    - #### **UnitProperty**

        - `UnitProperty`(...) : CUWP  
            Compile-time inserts a `Create Unit with Properties` into the map and returns it. You can use GetPropertyIndex to get its number. See the example for field explanations.

        Example

        ```JavaScript
        // All fields are optional  
        const prop = UnitProperty(
            hitpoint = 100,       // HP percentage 0~100  
            shield = 100,         // Shield percentage 0~100  
            energy = 100,         // Energy percentage 0~100  
            hanger = 0,           // 0~4294967295  
            resource = 0,         // 0~65536 (Count)  
            cloaked = False,      // Is invisible True/False
            burrowed = False,     // Is burrowed True/False
            intransit = False,    // Is being transported True/False
            hallucinated = False, // Is a hallucination True/False
            invincible = False    // Is invincible True/False
        );  
        CreateUnitWithProperties(1, "Terran Marine", $L("Location 3"), P1, prop);
        ```

    <br />

    - #### **GetPropertyIndex**

        - `GetPropertyIndex`(property : CUWP) : py_int  
            Compile-time gets the number of a CUWP [property] in the map CUWP list.

        Example

        ```JavaScript
        // All fields are optional
        const prop = UnitProperty(
            hitpoint = 100,       // HP percentage 0~100
        );
        py_print(GetPropertyIndex(prop));
        ```

    <br />

    - #### **GetPlayerInfo**

        - `GetPlayerInfo`(player: TrgPlayer) : py_struct  
            Compile-time gets the information of player [player] in the map information.[player] only supports constants. The information obtained is the information set in the map, not the runtime information.  

        Example

        ```JavaScript
        const pinfo = GetPlayerInfo(0);
        setcurpl(0);
        printAt(9, "Player 1 type:{}({}) race:{}({}) force:{}", pinfo.typestr, pinfo.type, pinfo.racestr, pinfo.race, pinfo.force);
        ```

    <br />

    - #### **EUDRegisterObjectToNamespace**

        - `EUDRegisterObjectToNamespace`(funcname, obj) : duck  
            Registers an object to the global namespace, mainly used for parameter passing between modules.

        Example

        ```JavaScript
        const menuSel = PVariable();
        EUDRegisterObjectToNamespace("menuSel", menuSel);
        ```

    <br />

    - #### **GetEUDNamespace**

        - `GetEUDNamespace()` : py_dict[str, duck]  
            Gets the global namespace dictionary, which records the objects registered in EUDRegisterObjectToNamespace. 

        Example

        ```JavaScript
        function afterTriggerExec() {
            setcurpl(P1);
            const menuSel2 = GetEUDNamespace().get("menuSel");
            println(9, "{}", menuSel2[0]);
        }
        ```

    <br />

    - #### **MPQAddFile**

        - `MPQAddFile`(fname, contents, isWave = false)  
            Adds a file named [fname] with byte content [contents] to the output map set by output. If [isWave] is set to true, it will be compressed using Wave lossy compression before importing.  

        Example

        ```JavaScript
        MPQAddFile("1.txt", py_open("C:/1.txt", "rb").read());
        ```

    <br />

    - #### **MPQAddWave**

        - `MPQAddWave`(fname, content)  
            It is equivalent to MPQAddFile(fname, contents, true).  

        Example

        ```JavaScript
        MPQAddWave("1.wav", py_open("C:/1.wav", "rb").read());
        ```


    <br />
    <br />


- ### Compile-time Python Macros

    In epScript, you can call all built-in functions of Python 3 with the py_ prefix. Here are some common ones.

    <br />

    - #### **py_print**

        - `py_print`(*args)  

            Compile-time uses Python's print function to print output content to the compile log interface for debugging output.  

        Example

        ```JavaScript
        py_print("This will only output to the CLI during compilation and has nothing to do with the map.");
        ```

        <br />

    - #### **py_list**

        - `py_list`(iter) : py_list  
            Creates and returns a compile-time Python list.  
            Compile-time lists can be iterated at compile time using foreach syntax, and their indices can only be constants.  

        Example

        ```JavaScript
        const lst = py_list();
        lst.append(DisplayText("11111"));
        lst.append(DisplayText("22222"));
        lst.append(DisplayText("33333"));
        DoActions(lst);
        ```

    <br />

    - #### **py_open**

        - `py_open`(filename, mode) : py_file  
            Compile-time opens the file [filename] in [mode] mode and returns a Python file object.  

        Example

        ```JavaScript
        function onPluginStart() {
            MPQAddWave("1.wav", py_open("C:/1.wav", "rb").read()); // Import an external file into the map
        }
        ```

    <br />

    - #### **py_eval**

        - `py_eval`(str) : duck  
            Simple Python code execution at compile time, returning the result.

        Example

        ```JavaScript
        import py_datetime;

        function is_map_expired() {
            static var expired = false;
            once {
                const expire_date = py_str('2024-01-01 00:00:00');
                const expire_date_stamp = py_eval("int(datetime.datetime.strptime(expire_date, '%Y-%m-%d %H:%M:%S').timestamp())");
                if (Memory(0x6D0F38, AtLeast, expire_date_stamp)) {
                    expired = true;
                }
            }
            return expired;
        }

        function onPluginStart() {
            if (is_map_expired()) {
                DisplayTextAll("This map has expired.");
            } else {
                DisplayTextAll("Have fun.");
            }
        }
        ```

    <br />

    - #### **py_str**

        - `py_str`(val) : py_str  
            Compile string wrapping conversion at compile time. 

        Example

        ```JavaScript
        const actions = py_list();
        foreach(i : py_range(0, 3)) {
            actions.append(CreateUnit(1, "Terran Marine", py_str("Location ") + py_str(i + 1), P1)); // Add an action to the list
        }
        DoActions(actions); // Execute all actions in the list at once
        ```

    <br />

    - #### **py_len**

        - `py_len`(gconstant) : py_int  
            Gets the length of global constants at the compile-time Python level.  

        Example

        ```JavaScript
        const lst = py_list();
        lst.append(DisplayText("11111"));
        lst.append(DisplayText("22222"));
        lst.append(DisplayText("33333"));
        foreach(i : py_range(0, py_len(lst))) {
            DoActions(lst[i]);
        }
        ```

    <br />

    - #### **py_enumerate**

        - `py_enumerate`(vlist) : py_iter  
            Compile-time enumeration iterator to enumerate and expand items in compile-time containers.  

        Example

        ```JavaScript
        var a, b, c, d;
        const list1 = list(a, b, c, d); // list is a compile-time container. Here it just puts the references of a/b/c/d together instead of the values of a/b/c/d.
        const list2 = list(15, 4, 99, 47);
        foreach(i, v : py_enumerate(list2)) {
            list1[i] = v;
        }
        println("{}, {}, {}, {}", a, b, c, d); // 15, 4, 99, 47
        ```

    <br />

    - #### **py_range**

        - `py_range`(start, end, step) : py_iter  
            Compile-time counting iterator to iterate from [start] to [end] in steps of [step] and expand the code block. Includes [start] but excludes [end].  

        Example

        ```JavaScript
        // https://armoha.github.io/eud-book/offsets/MouseCoordinateX.html
        // https://armoha.github.io/eud-book/offsets/MouseCoordinateY.html
        // The principle of reading memory values is to use 32 triggers to compare the value of each bit in 32 bits. If the i-th bit is greater than 0, the variable is appended with 2 to the power of i-1.
        function GetMouseXY() {
            var x, y;
            RawTrigger(actions = list(
                SetDeaths(EPD(x.getValueAddr()), SetTo, 0, 0),
                SetDeaths(EPD(y.getValueAddr()), SetTo, 0, 0),
            ));
            foreach(i : py_range(32)) { /* Use 64 triggers here to read mouse X Y values */
                RawTrigger(
                    conditions = DeathsX(EPD(0x6CDDC4), AtLeast, 1, 0, py_pow(2,i)),
                    actions = SetDeaths(EPD(x.getValueAddr()), Add, py_pow(2,i), 0),
                );
                RawTrigger(
                    conditions = DeathsX(EPD(0x6CDDC8), AtLeast, 1, 0, py_pow(2,i)),
                    actions = SetDeaths(EPD(y.getValueAddr()), Add, py_pow(2,i), 0),
                );
            }
            return x, y;
        }

        // The above GetMouseXY function is actually equivalent to the following
        function GetMouseXY() {
            return dwread(0x6CDDC4), dwread(0x6CDDC8);
        }
        ```


    <br />
    <br />

- ### Compile-time Bytes Conversion

    <br />

    - #### **b2i**

        - `b2i1`(content, index) : py_int  
        - `b2i1`(content, index) : py_int  
        - `b2i4`(content, index) : py_int  
            Converts the byte, word, or dword at position [index] in the literal byte string [content] to a positive integer constant using little endian.  

        Example

        ```JavaScript
        printAt(2, "0x{:x},0x{:x},0x{:x},0x{:x}", b2i1(b"fuck"), b2i1(b"fuck",1), b2i1(b"fuck",2), b2i1(b"fuck",3)); // 0x66, 0x75, 0x63, 0x6B
        printAt(3, "0x{:x},0x{:x},0x{:x}", b2i2(b"fuck"), b2i2(b"fuck",1), b2i2(b"fuck",2)); // 0x7566, 0x6375, 0x6B63
        printAt(4, "0x{:x}", b2i4(b"fuck")); // 0x6B637566
        ```

    <br />

    - #### **i2b**

        - `i2b1`(i) : py_byte  
        - `i2b2`(i) : [py_byte]  
        - `i2b4`(i) : [py_byte]  
            Converts the integer constant [i] to one, two or four byte constants using little endian.  

        Example

        ```JavaScript
        printAt(4, "{}", i2b4(0x6B637566));
        ```

    <br />

    - #### **u2b/b2u**

        - `u2b`(s) : [py_byte]  
        - `b2u`(b) : py_str  
            Converts between byte literal and string literal.  

        Example

        ```JavaScript
        printAt(5, "{}", u2b("fuck")); // b'fuck'
        printAt(6, "{}", b2u(b"fuck")); // fuck
        ```

    <br />

    - #### **UTF8 Encode/Decode**

        - `b2utf8`(str) : [py_byte]  
            Decodes [str] using UTF-8.  

        - `u2utf8`(str) : py_str  
            Encodes [str] using UTF-8. 

        Example

        ```JavaScript
        printAt(5, "{}", b2utf8("fuck")); // b'fuck'
        printAt(6, "{}", u2utf8(b"fuck")); // fuck
        ```

    <br />
    <br />
    

- ### General Functions

    <br />

    - #### **EPD**

        - `EPD`(ptr) : py_int | EUDVariable  
        Converts the specified pointer [ptr] to an EPD offset. In memory, the player number occupies 4 bytes (32-bit integer). It actually subtracts [ptr] from 0x58A364 and then divides by 4.  
        If the argument is a constant, the result can be returned at compile time.  

        Example

        ```JavaScript
        // https://armoha.github.io/eud-book/offsets/GameSpeedRefreshRate.html
        const epd = EPD(0x5124D8); // (0x5124D8-0x58A364)/4 = -0x1DFA3 = -122787
        ```

    <br />

    - #### **l2v**

        - `l2v`(conditionalExpression) : EUDVariable  
            Uses a trigger at runtime to get the logical value false or true of [conditionalExpression].  

        Example

        ```JavaScript
        var isP1MarineDeaths100 = l2v(Deaths(P1, AtLeast, 100, "Terran Marine"));
        ```

    <br />

    - #### **parse**

        - `parse`(address, radix=10) : py_list[EUDVariable, EUDVariable]  
            Parses a string at memory [address] into a number using [radix] notation.  
            Returns: number, digits  
            Returns 0, 0 on parse failure

        Example

        ```JavaScript
        const numstr = Db("102a\r\r\r\r\r\r\r\r\r\r\r\0");  
        var num, digits;  
        num, digits = parse(numstr, 8);  
        println("0x{:x}, {},  8 radix digits:{}", num, num, digits); // 0x00000042, 66,  8 radix digits:3
        num, digits = parse(numstr, 10);  
        println("0x{:x}, {}, 10 radix digits:{}", num, num, digits); // 0x00000066, 102, 10 radix digits:3
        num, digits = parse(numstr, 16);  
        println("0x{:x}, {}, 16 radix digits:{}", num, num, digits); // 0x0000102A, 4138, 16 radix digits:4
        ```

    <br />

    - #### **EUDFuncPtr**

        - `EUDFuncPtr`(argn, retn) : py_int  
            Declares a pointer to a closure function with [argn] arguments and [retn] return values.  

        - `EUDTypedFuncPtr`(argtypes, rettypes) : py_int  
            Declares a pointer to a closure function with an argument type list of [argtypes] and a return value type list of [rettypes].  

        Example

        ```JavaScript
        function GetMouseMapXY() {
            const screenX, screenY = dwread_epd(EPD(0x62848C)), dwread_epd(EPD(0x6284A8));
            const mouseX, mouseY = dwread_epd(EPD(0x6CDDC4)), dwread_epd(EPD(0x6CDDC8));
            const x, y = screenX + mouseX, screenY + mouseY;
            return x, y;
        }

        var funcptr = 0;

        function beforeTriggerExec() {
            static var x, y = 0, 0;
            once (funcptr == 0) {
                funcptr = EUDFuncPtr(0, 2)(function() {
                    x, y = GetMouseMapXY();
                    return x, y;
                });
            }

            setcurpl(P1);
            printAt(9, "before x = {}, y = {}", x, y);
        }

        function afterTriggerExec() {
            const x, y = EUDFuncPtr(0, 2).cast(funcptr)();
            setcurpl(P1);
            printAt(10, "after funcptr returns {}, {}", x, y);
        }
        ```

    <br />

    - #### **getgametick**

        - `getgametick()` : EUDVariable  
            Gets the number of game frames elapsed. At the `Fastest` game speed, it is 42 milliseconds per frame.  

        Example

        ```JavaScript
        var tick = getgametick();
        ```

    <br />
    <br />

- ### Trigger Construction Functions

    Trigger construction functions can be used to construct triggers with custom properties.

    <br />

    - #### **RawTrigger**

        - `RawTrigger`(conditions = list(...), actions = list(...), preserved = true/false) : RawTrigger  
            Inserts a static classical trigger and cannot pass variables. Returns a trigger pointer.  
            The conditions field passes a list of constant conditional expressions with a maximum of 16 classical trigger conditions.  
            The actions field passes a list of constant action expressions with a maximum of 64 classical trigger actions.  
            The preserved field defaults to true, indicating that it will execute each time it is called. If set to false, it will execute once after the condition is met and will never execute again.  

        Example

        ```JavaScript
        // https://armoha.github.io/eud-book/offsets/MouseCoordinateX.html
        // https://armoha.github.io/eud-book/offsets/MouseCoordinateY.html
        // The principle of reading memory values is to use 32 triggers to compare the value of each bit in 32 bits. If the i-th bit is greater than 0, the variable is appended with 2 to the power of i-1.
        function GetMouseXY() {
            var x, y;
            RawTrigger(actions = list(
                SetDeaths(EPD(x.getValueAddr()), SetTo, 0, 0),
                SetDeaths(EPD(y.getValueAddr()), SetTo, 0, 0),
            ));
            foreach(i : py_range(32)) { /* Use 64 triggers here to read mouse X Y values */
                RawTrigger(
                    conditions = DeathsX(EPD(0x6CDDC4), AtLeast, 1, 0, py_pow(2,i)),
                    actions = SetDeaths(EPD(x.getValueAddr()), Add, py_pow(2,i), 0),
                );
                RawTrigger(
                    conditions = DeathsX(EPD(0x6CDDC8), AtLeast, 1, 0, py_pow(2,i)),
                    actions = SetDeaths(EPD(y.getValueAddr()), Add, py_pow(2,i), 0),
                );
            }
            return x, y;
        }

        // The above GetMouseXY function is actually equivalent to the following
        function GetMouseXY() {
            return dwread(0x6CDDC4), dwread(0x6CDDC8);
        }
        ```

    <br />

    - #### **Trigger**

        - `Trigger`(conditions = list(...), actions = list(...), preserved = true/false)  
            Inserts an extended trigger, which may be split into many classical triggers. It is not limited to 16 conditions and 64 actions, and variables can be passed in, but no return value is returned.  
            Passing variables will not take effect dynamically before the actions are completed, and will only maintain the state of the variables when the trigger starts executing.  
            For clarity of code, it is generally recommended not to use Trigger and instead use if conditions to complete dynamic conditional comparisons.  
            The conditions field passes a list of conditional expressions.  
            The actions field passes a list of action expressions.  
            The preserved field defaults to true, indicating that it will execute each time it is called. If set to false, it will execute once after the condition is met and will never execute again.  

        Example

        ```JavaScript
        Trigger(
            conditions = list(
                Bring(P1, AtMost, 0, "Zerg Cerebrate", "Location 1")
            ),
            actions = list(
                KillUnitAt(All, "Terran Medic", "Location 1", P1)
            ),
            preserved = false,
        );
        ```

    <br />

    - #### **PTrigger**

        - `PTrigger`(players, conditions = list(...), actions = list(...))  
            Inserts a trigger that matches the current player. When the `current player` is any of the players in [players], it will execute. There is no preserved field, and the other fields are used in the same way as Trigger. 

        Example

        ```JavaScript
        setcurpl(P8);
        PTrigger(list(P3, P8),
            conditions = ElapsedTime(AtLeast, 3),
            actions = KillUnit($U("Terran Medic"), P1),
        );
        ```

    <br />

    - #### **DoActions**

        - `DoActions`(actions, preserved = true/false)  
            A Trigger function that executes actions unconditionally.  
            In epScript, any non-comment code between two semicolons is automatically wrapped in this function as a trigger.  
            actions is a list of action expressions.  
            The preserved field defaults to true, indicating that it will execute each time it is called. If set to false, it will execute once after the condition is met and will never execute again.  

        Example

        ```JavaScript
        Order("Zerg Hydralisk", P8, $L("UpArea"), Patrol, "Player1Home"); // If a line of code is only a trigger action function call, it will be wrapped in a DoActions after compilation.  

        DoActions(Order("Zerg Hydralisk", P8, $L("UpArea"), Patrol, "Player1Home"));  

        DoActions(list(// To be more explicit, you can add list  
            Order("Zerg Hydralisk", P8, $L("UpArea"), Patrol, "Player1Home"),  
        ));  

        Trigger(actions = list(  
            Order("Zerg Hydralisk", P8, $L("UpArea"), Patrol, "Player1Home"),  
        ));

        // The above four usages are completely equivalent  

        const a = Order("Zerg Hydralisk", P8, $L("UpArea"), Patrol, "Player1Home"); // This line of code is not equivalent to the above usages. It is used to declare an action expression constant named a, which will not be automatically wrapped in DoActions.  

        DoActions(  
            Order("Zerg Guardian", P8, $L("UpArea"), Patrol, "Player1Home"),  
            Order("Zerg Guardian", P8, $L("MiddleArea"), Patrol, "Player1Home"),  
            Order("Zerg Devourer", P8, $L("UpArea"), Patrol, "Player1Home"),  
            Order("Zerg Devourer", P8, $L("MiddleArea"), Patrol, "Player1Home"),  
            preserved = false, // The preserved parameter must be a named parameter  
        );  

        // Static Feature Demo  
        // The variables passed to the actions of DoActions will be replaced with a static constant value when DoActions starts executing. No matter how many times the variable is modified during the execution of DoActions, the passed in value is determined before execution.  
        var c = 0;  
        c.AddNumber(1);  
        DoActions(  
            c.AddNumber(100),  
            CreateUnit(c, "Terran SCV", "Location 2", P1),  
        );  
        printAt(10, "You would expect to create {} SCVs, but only 1 was actually created", c); // You would expect to create 100 SCVs here, but only 1 was actually created
        ```

    <br />

    - #### **VProc**

        - `VProc`(vars, actions) : RawTrigger | [RawTrigger]  
            The action list [actions] can only pass constant action expression lists. VProc will execute all the virtual triggers of the variables in [vars] in order after executing all the actions in [actions] in order.  
            This means that the virtual triggers of some variables can first be modified in [actions], and then the modified virtual triggers of these variables will be executed by VProc after the actions are completed.  
            It is usually used to optimize the overhead of serial assignment or bitwise operations on variables. Its overhead is slightly higher than RawTrigger but lower than DoActions or Trigger.  
            A virtual trigger of a variable can only have one SetDeathsX action. If multiple actions are queued to the variable queue, the last one is taken.  

            [Variable Operation Optimization](../How-epScript-Works.md#variable-operation-optimization)

        Example

        ```JavaScript
        var unrelatedVariable = 0;  
        var c, d = 0, 0;  

        c = 1;  
        RawTrigger(actions = list(  
            c.AddNumber(100),  
            c.QueueAssignTo(d),  
        ));  
        println("After RawTrigger process c:{} d:{}", c, d); // c:101 d:0  

        c = 1;  
        VProc(c, list(  
            c.AddNumber(100),
            c.QueueAssignTo(d),  
        ));  
        println("After VProc(c) process c:{} d:{}", c, d); // c:101 d:101  

        c = 1;  
        VProc(list(c, d), list(  
            c.AddNumber(100),  
            c.QueueAssignTo(d),  
            d.QueueAddTo(c),  
        ));  
        println("After VProc(c,d) process c:{} d:{}", c, d); // c:202 d:101  

        c = 1;  
        VProc(list(d, c), list(  
            c.AddNumber(100),  
            c.QueueAssignTo(d),  
            d.QueueAddTo(c),  
        ));  
        println("After VProc(d,c) process c:{} d:{}", c, d); // c:202 d:202
        ```


    <br />
    <br />

- ### Runtime Iterators

    Runtime iterators can be used with the compile-time loop syntax foreach to construct a runtime loop. The number of times it executes is controlled by the internal flow control logic of the iterator.  
    break and continue can be used in the foreach code block belonging to the runtime iterator, and they will be compiled into EUDContinue() and EUDBreak().  
    Let's explain the principle of runtime iterators in an equivalent code way. For example, there is the following code:  

    ```JavaScript
    foreach (cu : EUDLoopNewCUnit()) {
        py_print(cu);
        println("{}", cu);
        continue;
    }
    ```

    It is roughly equivalent to:  

    ```JavaScript
    {  
        const it = EUDLoopNewCUnit();  
        const cu = py_next(it); // The first compile-time iteration gets the storage location of the iteration result and sets the start of the EUD runtime loop code block, equivalent to an EUDWhile()(the runtime it has a next item)  
            py_print(cu);       // Compile-time output, will only execute once  
            println("{}", cu);       
            EUDContinue();  
        py_next(it, 0);         // The second compile-time iteration sets the end position of the EUD runtime loop code block, equivalent to an EUDEndWhile()  
    }
    ```

    <br />

    - #### **EUDLoopPlayer**

        - `EUDLoopPlayer`(ptype, force, race) : EUDIterator  
            Iterates over active players of type [ptype], force [force] and race [race]. Internally uses playerexist to detect.  
            Active players do not include vacant or leaving players.  

        Example

        ```JavaScript
        // ptype is an optional parameter, can be "Human" or "Computer"  
        // force is an optional parameter, can be Force1 Force2 Force3 Force4  
        // race  is an optional parameter, can be "Zerg" "Terran" "Protoss"
        foreach (p: EUDLoopPlayer("Human", Force1, "Zerg")) {
            setcurpl(p);
            println("You are Zerg");
        }
        ```

    <br />

    - #### **EUDLoopRange**

        - `EUDLoopRange`(start, end=None) : EUDIterator  
            Iterates over values from [start] to [end] - 1.  

        Example

        ```C#
        // Print 1 to 4
        foreach (i : EUDLoopRange(1, 5)) {
            simpleprint(i);
        }
        // The above code is roughly equivalent to
        for (var i = 1; i < 5; i++) {
            simpleprint(i);
        }
        ```

    <br />

    - #### **EUDLoopUnit**

        - `EUDLoopUnit()` : EUDIterator  
            Iterates over the ptr and epd of all units on the main chain. 
            Does not include subunits, Scanner Sweep, Map Revealer, etc.  

        Example

        ```JavaScript
        foreach (ptr, epd : EUDLoopUnit()) {
            const u = CUnit(epd);
            if (u.unitID == $U("Terran Marine")) {
                u.hp = 0x100 * 10;
            }
        }
        ```

        <br />

        - `EUDLoopUnit2()` : EUDIterator  
            Iterates over the ptr and epd of all units.  
            Does not include subunits, Scanner Sweep, Map Revealer, etc.  

        Example

        ```JavaScript
        // The Unit Node Table is a doubly linked list with a main chain and branch chains.  
        // FirstUnitPointer -> Unit1 <-> Unit2 <-> "Terran Siege Tank" <-> Unit4 -> Null  
        //                                                   |   
        //                                              "Tank Turret"  
        // The main chain and branch chains both occupy memory space. For example, in the above example, Bring will determine that there are a total of 4 units, but in fact 5 of the 1700 unit spaces are occupied.  
        // EUDLoopUnit() will only loop the units on the main chain, so it will ignore "Tank Turret" - the tank turret.  
        // EUDLoopUnit2() will loop all units occupying the Unit Node Table space, because it does not loop in the order of the linked list, but in the order of memory.  
        // EUDLoopUnit(): Loop along the main chain unit, unable to loop to sub unit and map revealer, etc.  
        // EUDLoopUnit2(): Loop along the Memory index to loop all units.  
        foreach (ptr, epd : EUDLoopUnit2()) {  
            const u = CUnit(epd);  
            if (u.unitID == $U("Terran Marine")) {  
                u.hp = 0x100 * 10;  
            }  
        }
        ```

        <br />

        - `EUDLoopCUnit()` : EUDIterator  
            It uses EUDLoopUnit2 to traverse and wraps the traversed pointers into CUnit objects.  
            Does not include subunits, Scanner Sweep, Map Revealer, etc.

        Example

        ```JavaScript
        foreach (u : EUDLoopCUnit()) {
            if (u.unitID == $U("Terran Marine")) {
                u.hp = 0x100 * 10;
            }
        }
        ``` 

        <br />

        - `EUDLoopNewUnit`(allowance = 2) : EUDIterator  
            Iterates over up to [allowance] ptr and epd of new units that have appeared since the last time `current frame` called EUDLoopNewUnit or EUDLoopNewCUnit.  
            Does not include subunits, Scanner Sweep, Map Revealer, etc.  

        - `EUDLoopNewCUnit`(allowance = 2) : EUDIterator  
            Iterates over up to [allowance] new units that have appeared since the last time `current frame` called EUDLoopNewUnit or EUDLoopNewCUnit and wraps the traversed pointers into CUnit objects.  
            Does not include subunits, Scanner Sweep, Map Revealer, etc.  

        > **Warning**  
        > Calling EUDLoopNewUnit or EUDLoopNewCUnit multiple times in the same frame will traverse the same units.  
        > Zerg peculiarity: New units are only larvae, cancelled Zerg Extractor drones, the second unit of twin units (zergling, scourges, Nydus canal), and any units created out of thin air using the CreateUnit function.   

        > **Note**  
        > The hatching process of Zerg eggs will use the address of the larva. The hatched unit will continue to use this address. If it is hatching a dog, one of the dogs will continue to use the larva's address and the other will be a new unit. Scourges are similar.  
        > Buildings hatched by Zerg drones will use the drone's address. Cancelling the hatch will turn back into a drone with the same address and will not produce a new unit.  
        > For an instant when a drone hatches into a Zerg Extractor, it will inherit the address of the Vespene Geyser unit (the Vespene Geyser itself is a unit). The drone is considered dead. If the construction is cancelled, a new drone is returned. This drone can be traversed.   
        > Units queued in the barracks: they are only detected when they walk out after completion.   
        > Buildings: Can be detected as soon as construction starts (unfinished construction).   
        > Archons and Dark Archons: After Templars merge, the Archon will use the address of one of the Templars. The other Templar is considered dead and will not produce a new unit. Dark Archons are similar.

        Example

        ```JavaScript
        foreach (ptr, epd : EUDLoopNewUnit(1700)) {
            const u = CUnit(epd);
            if (u.unitID == $U("Terran Marine")) {
                u.hp = 0x100 * 10;
            }
        }

        foreach (u : EUDLoopNewCUnit(1700)) {
            if (u.unitID == $U("Terran Marine")) {
                u.hp = 0x100 * 10;
            }
        }

        // The following code is a complete traversal of new units, the code comes from: GGRush
        const NewUnits = UnitGroup(1000);
        const ChangeableUnits = EUDDeque(1000)();

        function onPluginStart() {
            GetGlobalStringBuffer();
        }

        function beforeTriggerExec() {
            foreach(cunit: EUDLoopNewCUnit()) {
                NewUnits.add(cunit);
            }

            ChangeableUnits.append(-1);
            var uid, value;
            while(True) {
                value = ChangeableUnits.popleft();
                if(value == -1) break;
                else if(value < 228) uid = value;
                else if(value >= EPD(0x59CCA8)) {
                    const epd = value;
                    if(!MemoryXEPD(epd + 0x64/4, Exactly, prev, 0xFFFF)) NewUnits.add(value); 
                    else {
                        ChangeableUnits.append(uid);
                        ChangeableUnits.append(epd);
                    }
                }
            }

            foreach(unit: NewUnits.cploop) {
                foreach(dead: unit.dying) {}	// Existence check: living units continue to execute code, dead units continue
                unit.move_cp(0x64/4);
                if(DeathsX(CurrentPlayer, Exactly, $U("Zerg Larva"), 0, 0xFFFF)
                || DeathsX(CurrentPlayer, Exactly, $U("Zerg Egg"), 0, 0xFFFF)
                || DeathsX(CurrentPlayer, Exactly, $U("Zerg Drone"), 0, 0xFFFF)
                || DeathsX(CurrentPlayer, Exactly, $U("Zerg Hydralisk"), 0, 0xFFFF)
                || DeathsX(CurrentPlayer, Exactly, $U("Zerg Lurker Egg"), 0, 0xFFFF)
                || DeathsX(CurrentPlayer, Exactly, $U("Zerg Mutalisk"), 0, 0xFFFF)
                || DeathsX(CurrentPlayer, Exactly, $U("Mutalisk Cocoon"), 0, 0xFFFF)
                || DeathsX(CurrentPlayer, Exactly, $U("Zerg Hatchery"), 0, 0xFFFF)
                || DeathsX(CurrentPlayer, Exactly, $U("Zerg Lair"), 0, 0xFFFF)
                || DeathsX(CurrentPlayer, Exactly, $U("Zerg Creep Colony"), 0, 0xFFFF)
                || DeathsX(CurrentPlayer, Exactly, $U("Zerg Spire"), 0, 0xFFFF)
                || DeathsX(CurrentPlayer, Exactly, $U("Protoss High Templar"), 0, 0xFFFF)
                || DeathsX(CurrentPlayer, Exactly, $U("Protoss Dark Templar (Unit)"), 0, 0xFFFF)
                ) {
                    const uid = wread_cp(0, 0);
                    ChangeableUnits.append(uid);
                    ChangeableUnits.append(unit.epd);
                }
                // start
                // Your codes
                // end
                unit.remove();	//This code is necessary!!!Don't skip it
            }
        }
        ```

        <br />

        - `EUDLoopPlayerUnit`(player: TrgPlayer) : EUDIterator  
            Iterates over all units of player [player] ptr and epd.

        - `EUDLoopPlayerCUnit`(player: TrgPlayer) : EUDIterator  
            Iterates over all units of player [player] and wraps the traversed pointers into CUnit objects.

        Example

        ```JavaScript
        foreach (ptr, epd : EUDLoopPlayerUnit(P1)) {
            const u = CUnit(epd);
            if (u.unitID == $U("Terran Marine")) {
                u.hp = 0x100 * 10;
            }
        }

        foreach (u : EUDLoopPlayerCUnit(P1)) {
            if (u.unitID == $U("Terran Marine")) {
                u.hp = 0x100 * 10;
            }
        }

        // Change all Marines of Owner player to NewOwner player
        // Using cunit.give will affect the iteration of EUDLoopPlayerCUnit, so you need to first add all cunits to a queue container
        // and then change the owner of each cunit from the container
        const givequeue = EUDQueue(100);
        foreach(cunit: EUDLoopPlayerCUnit(Owner)) {
            if(cunit.unitType != $U("Terran Marine")) continue;
            givequeue.append(cunit);
        }
        while (!givequeue.empty()) {
            const cunit = CUnit(givequeue.pop());
            cunit.cgive(NewOwner);
        }
        ```

    <br />
    <br />

- ### Display Text Functions

    <br />

    - #### **DisplayTextAt**

        - `DisplayTextAt`(line, text : TrgString)  
            Displays [text] on line [line] of the `Local Player == Current Player` screen  
            It is different from DisplayText and does not return a trigger action expression  

        - `DisplayTextAllAt`(line, text : TrgString)  
            Displays [text] on line [line] for all players (including observers) 
            It is different from DisplayTextAll and does not return a trigger action expression  

        Example

        ```JavaScript
        var text_10 = $T("_10");
        var text_09 = $T("_09");
        var line = 10;
        DisplayTextAllAt(line, text_10);
        line -= 1;
        DisplayTextAllAt(line, text_09);
        line -= 1;
        setcurpl(P1);
        DisplayTextAt(line, "Only displayed to P1");
        ```

    <br />

    - #### **print**

        - `simpleprint`(*args, spaced=true)  
            Prints multiple arguments [*args] in order on the next line of the `Local Player == Current Player` screen scroll information. The named argument spaced indicates whether to separate each printed argument with spaces, the default is true. 

        - `println`(format_string : py_str, *args)  
            Prints multiple arguments [*args] formatted according to [format_string] on the next line of the `Local Player == Current Player` screen scroll information.

        - `printAt`(line, format_string : py_str, *args)  
            Prints multiple arguments [*args] formatted according to [format_string] on line [line] from top to bottom (range 0~10) of the `Local Player == Current Player` screen scroll information.

        - `printAll`(format_string : py_str, *args)  
            Prints multiple arguments [*args] formatted according to [format_string] on the next line of all player screen scroll information.

        - `printAllAt`(line, format_string : py_str, *args)  
            Prints multiple arguments [*args] formatted according to [format_string] on line [line] from top to bottom (range 0~10) of all player screen scroll information.

        <details>

        <summary>Formatting placeholders</summary>

        - `{}`: Generic placeholder used to output the value or constant pointer of a variable  
        - `{{}}`: Outputs `{}` itself  
        - `{:c}`: Outputs the value at the position as the player ID in the corresponding player color code, like PColor(the value at the position)  
        - `{:n}`: Outputs the value at the position as the player ID in the corresponding player name, like PName(the value at the position)  
        - `{:s}`: Outputs the value at the position as a string pointer to the string it points to, like ptr2s(the value at the position)  
        - `{:t}`: Outputs the value at the position as an EPD string pointer to the string it points to, like epd2s(the value at the position)  
        - `{:x}`: Outputs the numeric value at the position as an 8-digit hexadecimal number left-padded with 0's, like hptr(the numeric value at the position)  
        </details>

        Example

        ```JavaScript
        // simpleprint(*args, spaced=true)  
        simpleprint("Hello", "Starcraft");                  // Prints "Hello Starcraft" on the next line of the current player's screen scroll information.  
        simpleprint("Hello", "Starcraft", spaced = false);  // Prints "HelloStarcraft" on the next line of the current player's screen scroll information.  
        
        // println(format_string, *args)  
        println("{} {}", "Hello", "Starcraft");             // Prints "Hello Starcraft" on the next line of the current player's screen scroll information.  
        
        // printAt(line, format_string, *args)  
        printAt( 0, "{} {}", "Hello", "Starcraft");         // Prints "Hello Starcraft" on the top line of the current player's screen scroll information.  
        printAt(10, "{} {}", "Hello", "Starcraft");         // Prints "Hello Starcraft" on the bottom line of the current player's screen scroll information.  
        
        // printAll(format_string, *args)  
        printAll("{} {}", "Hello", "Starcraft");            // Prints "Hello Starcraft" on the next line of all players' screen scroll information.  
        
        // printAllAt(line, format_string, *args)  
        printAllAt( 0, "{} {}", "Hello", "Starcraft");      // Prints "Hello Starcraft" on the top line of all players' screen scroll information.  
        printAllAt(10, "{} {}", "Hello", "Starcraft");      // Prints "Hello Starcraft" on the bottom line of all players' screen scroll information.
        ```

    <br />

    - #### **GetGlobalStringBuffer**

        - `GetGlobalStringBuffer()` : StringBuffer  
            Gets the StringBuffer used internally by the print series functions of `Local Player == Current Player`. Its capacity is 1023 bytes.

        Example

        ```JavaScript
        // The following two lines of code are equivalent  
        printAt( 0, "{} {}", "Hello", "Starcraft");  
        GetGlobalStringBuffer().printfAt(0, "{} {}", "Hello", "Starcraft");
        ```

    <br />

    - #### **eprint**

        - `eprintln`(*args)  
            Prints multiple arguments [*args] in order to the error message below the center of the `current player`'s screen. Printing more than 218 bytes of content (including color code string endings, etc.) will cause an error. 

        - `eprintf`(format_string, *args)  
            Prints multiple arguments [*args] formatted according to the literal string [format_string] to the error message below the center of the `current player`'s screen. Printing more than 218 bytes of content (including color code string endings, etc.) will cause an error.

        - `eprintAll`(format_string, *args)  
            Prints multiple arguments [*args] formatted according to the literal string [format_string] to the error message below the center of all players' screens. Printing more than 218 bytes of content (including color code string endings, etc.) will cause an error. 

        - `eprintln2`(*args)  
            Prints multiple arguments [*args] in order to the error message below the center of the `current player`'s screen.   
            Replaces stat_txt.tbl[871]: "Unit's waypoint list is full." This error message, then coordinates with QueueGameCommand_QueuedRightClick(xy) can output more than 218 bytes of content in the error message.

        <details>

        <summary>Formatting placeholders</summary>

        - `{}`: Generic placeholder used to output the value or constant pointer of a variable  
        - `{{}}`: Outputs `{}` itself  
        - `{:c}`: Outputs the value at the position as the player ID in the corresponding player color code, like PColor(the value at the position)  
        - `{:n}`: Outputs the value at the position as the player ID in the corresponding player name, like PName(the value at the position)  
        - `{:s}`: Outputs the value at the position as a string pointer to the string it points to, like ptr2s(the value at the position)  
        - `{:t}`: Outputs the value at the position as an EPD string pointer to the string it points to, like epd2s(the value at the position)  
        - `{:x}`: Outputs the numeric value at the position as an 8-digit hexadecimal number left-padded with 0's, like hptr(the numeric value at the position)  
        </details>

        Example

        ```JavaScript
        eprintln("Hello", "Starcraft");                  // Prints "HelloStarcraft" to the error message below the center of the current player's screen.  
        eprintf("{}-{}", "Hello", "Starcraft");          // Prints "Hello-Starcraft" to the error message below the center of the current player's screen.  
        eprintAll("{}-{}", "Hello", "Starcraft");        // Prints "Hello-Starcraft" to the error message below the center of all players' screens. 
        ```

    <br />

    - #### **TextFX**

        - TextFX_FadeIn(*args, color=None, wait=1, reset=True, tag=None, encoding="UTF-8")  
            Fade in text effect

        - TextFX_FadeOut(*args, color=None, wait=1, reset=True, tag=None, encoding="UTF-8")  
            Fade out text effect

        - `TextFX_Remove`(tag)  
            Removes the text effect with the local tag [tag]

        - `TextFX_SetTimer`(tag, SetTo/Add/Subtract : TrgModifier, value)  
            Sets the timer of the text effect with the local tag [tag] to [SetTo/Add/Subtract] [value]


    <br />
    <br />

- ### Players Functions

    <br />

    - #### **getuserplayerid**

        - `getuserplayerid()` : EUDVariable  
            Gets the local player ID. The local player is not the `current player`. The local player ID obtained on each player's computer is different. It returns `desync-data`

        Example

        ```JavaScript
        setcurpl(getuserplayerid());
        println("The ID of the current player: {}", getuserplayerid());
        ```

    <br />

    - #### **playerexist**

        - `playerexist`(player) : EUDVariable  
            Checks if player [player] still exists in the game. Computer players are also players.

        Example

        ```JavaScript
        if (playerexist(P1)) {
            // Player 1 exists
        }
        ```

    <br />

    - #### **Current Player**

        - `getcurpl()` : EUDVariable  
            Gets the value of cpcache. If cpcache has no value or cpcache's value is different from the `current player`, the value of the `current player` is cached in cpcache and returned. 

        - `setcurpl`(cp)  
            Sets the value of the `current player` to [cp] and caches it in cpcache.

        - `addcurpl`(n)  
            Increments the value of the `current player` by [n] and caches it in cpcache.

        - `setcurpl2cpcache()`  
            Restores the value of the `current player` to the cached value in cpcache.   

        The `current player` can be thought of as a global variable. Specifying the player ID as CurrentPlayer(13) in trigger conditions or actions that require a specific player ID will use it. Some trigger actions internally use it. The `current player` may not even refer to a player and may store any value.

        <details>

        <summary>Actions that only take effect on the machine where current player == local player (allow desync use, can be used separately on some player machines)</summary>

        - DisplayText  
        - CenterView  
        - PlayWAV  
        - MinimapPing  
        - TalkingPortrait  
        - Transmission  
        - SetMissionObjectives  
        </details>

        <details>

        <summary>Actions that use current player as a parameter (must be synchronized on all player machines, otherwise disconnected)</summary>

        - SetAllianceStatus  
        - RunAIScript  
        - RunAIScriptAt  
        - Draw  
        - Defeat  
        - Victory  
        </details>

        Example

        ```JavaScript
        const cp = getcurpl();  
        setcurpl(P1);  
        println("Hello Player 1");  
        setcurpl(cp);  

        // CurrentPlayer is the constant number 13, which can cause some player-related conditions or actions to access the value of the current player
        // CurrentPlayer != getcurpl()

        // https://armoha.github.io/eud-book/offsets/GameSpeedRefreshRate.html
        setcurpl(-122787); // PlayerID offset for game speed level 1
        addcurpl(6); // Game speed level 7
        SetDeaths(CurrentPlayer, SetTo, 21, 0); // Game speed x2

        // https://armoha.github.io/eud-book/offsets/TriggerCurrentPlayerakaCPTrick.html
        // https://armoha.github.io/eud-book/offsets/GameBrightness.html
        SetMemory(0x6509B0, SetTo, 210382); // Change the current player to 210382 (game brightness level 0~31)
        SetDeaths(CurrentPlayer, SetTo, 15, 0); // Set brightness to 15
        setcurpl2cpcache(); // Restore the current player to cpcache to prevent interference with getcurpl and other functions
        ```

    <br />

    - #### **PColor**

        - `PColor`(player: TrgPlayer) : Db*  
            Returns player [player]'s color code in the game. Using the formatting placeholder `{:c}` in formatted text is equivalent. 

    <br />

    - #### **PName**

        - `PName`(player: TrgPlayer) : Db*  
            Returns player [player]'s name in the game. Using the formatting placeholder `{:n}` in formatted text is equivalent. 

        Example

        ```JavaScript
        println("Player 1: {}{}", PColor(P1), PName(P1)); // If Player 1 is named Soze and the color is red, this output will print the red Soze
        println("Player 1: {:c}{:n}", P1, P1);            // Equivalent to the above
        ```

    <br />

    - #### **SetPName**

        - `SetPName`(player : TrgPlayer, *args)  
            Sets [player]'s name to the text composed of multiple arguments [*args].  

        - `SetPNamef`(player: TrgPlayer, format_string, *args)  
            Sets [player]'s name to the text formatted by multiple arguments [*args] using [format_string].  

        Both functions do not affect the name obtained by the PName function. They only affect the name displayed in player chat, and only valid for the current frame. They need to be re-run every frame.  

        Example

        ```JavaScript
        // The following two usages are equivalent
        SetPName(cp, epd2s(title), " \x07level: \x04", level, " ", PColor(cp), PName(cp));
        SetPNamef(cp, "{:t} \x07level: \x04{} {:c}{:n}", title, level, cp, cp);
        ```

    <br />

    - #### **EUDPlayerLoop**

        - `EUDPlayerLoop()()`  
        - `EUDEndPlayerLoop()`  
            These two are a pair. It will sequentially set the `current player` to each active player (including computer players). After completion, the value of the current player will be the value before the Loop started.  

        Example

        ```JavaScript
        // Give all players 1000 ore minerals, including computer players
        EUDPlayerLoop()();
            SetResources(CurrentPlayer, Add, 1000, Ore);
        EUDEndPlayerLoop();
        ```

    <br />
    <br />

- ### Location Functions

    <br />

    - #### **setloc**

        - `setloc`(loc : TrgLocation, x, y)  
            Sets the upper left and lower right coordinates of location [loc] to [x], [y], [x], [y] respectively (that is, set the location to a point).  

        - `setloc`(loc : TrgLocation, left, top, right, bottom)  
            Sets the upper left and lower right coordinates of location [loc] to [left], [top], [right], [bottom] respectively.  

        Example

        ```JavaScript
        setloc($L("Location 1"), 1234, 2345);
        setloc($L("Location 1"), 1234, 1234, 2345, 2345);
        ```

    <br />

    - #### **addloc**

        - `addloc`(loc : TrgLocation, x, y)  
            Sets the left and right coordinates of location [loc] to add [x] and the up and down coordinates to add [y] (the actual size remains unchanged, the center moves to another position).  

        - `addloc`(loc : TrgLocation, left, top, right, bottom)  
            Sets the upper left, upper right, lower left and lower right of location [loc] to add [left], [top], [right], [bottom] respectively.  

        Example

        ```JavaScript
        addloc($L("Location 1"), 123, 234);
        addloc($L("Location 1"), 123, 234, 345, 456);
        // Used with lengthdir  
        addloc($L("Location 1"), lengthdir_256(888, 73)); // Move Location 1 area 888 coordinates in the 73 degree (256 degree system) direction  
        addloc($L("Location 1"), lengthdir(888, 102)); // Move Location 1 area 888 coordinates in the 102 degree direction
        ```

    <br />

    - #### **dilateloc**

        - `dilateloc`(loc : TrgLocation, x, y)  
            Sets the upper left, upper right, lower left and lower right of location [loc] to add -[x], -[y], [x], [y] respectively (the center remains unchanged, the area expands).  

        - `dilateloc`(loc : TrgLocation, left, top, right, bottom)  
            Sets the upper left, upper right, lower left and lower right of location [loc] to add -[left], -[top], [right], [bottom] respectively.  

        Example

        ```JavaScript
        dilateloc($L("Location 1"), 5, 5);
        dilateloc($L("Location 1"), 1, 2, 3, 4);
        ```

    <br />

    - #### **getlocTL**

        - `getlocTL`(loc : TrgLocation) : py_tuple[EUDVariable, EUDVariable]  
            Gets the upper left coordinate of a location.  

        Example

        ```JavaScript
        const left, top = getlocTL($L("Location 1"));
        ```

    <br />

    - #### **setloc_epd**

        - `setloc_epd`(loc : TrgLocation, epd)  
            Sets the coordinates of location [loc] to the value stored at local memory address `0x58A364 + [epd] * 4`.  

        Example

        ```JavaScript
        // It is same as the following function
        function setloc_epd(loc : TrgLocation, epd) {
            const x, y = posread_epd(epd);
            setloc(loc, x, y);
        }
        ```

    <br />
    <br />

- ### Memory Operation Functions

    <br />

    - #### **dwbreak**

        - `dwbreak`(number) : py_tuple[EUDVariable, EUDVariable, EUDVariable, EUDVariable, EUDVariable, EUDVariable]  
            Splits a dword value [number] into word and byte forms.  

        Example

        ```JavaScript
        const w1, w2, b1, b2, b3, b4 = dwbreak(1234 + 0x10000 * 5678)[[0,1,2,3,4,5]];
        println("w1:{} w2:{} b1:{} b2:{} b3:{} b4:{}", w1, w2, b1, b2, b3, b4);
        ```

    <br />

    - #### **read/write**

        - `dwread`(ptr) : EUDVariable  
        - `wread`(ptr) : EUDVariable  
        - `bread`(ptr) : EUDVariable  

            Reads the dword/word/byte value at the specified local memory address [ptr].    

        - `dwwrite`(ptr, dw)  
        - `wwrite`(ptr, w)  
        - `bwrite`(ptr, b)  

            Writes dword/word/byte values to local memory address [ptr].  

        Example

        ```JavaScript
        // 0x582144: https://armoha.github.io/eud-book/offsets/ZergControlAvailable.html
        const SUP_RACE_ZERG = 0;
        const SUP_RACE_TERRAN = 1;
        const SUP_RACE_PROTOSS = 2;
        const SUP_TYPE_AVAILABLE = 0;
        const SUP_TYPE_USED = 1;
        const SUP_TYPE_MAX = 2;

        function SetPlayerSupply(player: TrgPlayer, race, type, amount) {
            dwwrite(0x582144 + (race) * 36 * 4 + (type) * 12 * 4 + (player) * 4, amount);
        }
        function GetPlayerSupply(player: TrgPlayer, race, type) {
            return dwread(0x582144 + (race) * 36 * 4 + (type) * 12 * 4 + (player) * 4);
        }

        SetPlayerSupply(P1, SUP_RACE_ZERG, SUP_TYPE_MAX, 800); // Set player 1's Zerg supply maximum to 400
        ```

    <br />

    - #### **read_epd/write_epd**

        - `dwread_epd`(epd) : EUDVariable  
            Reads the dword value at local memory address `0x58A364 + [epd] * 4`.  

        - `dwwrite_epd`(epd, value)  
            Writes a dword value to local memory address `0x58A364 + [epd] * 4`.  

        - `wread_epd`(epd, subp) : EUDVariable  
        - `bread_epd`(epd, subp) : EUDVariable  

            Reads the word/byte value at local memory address `0x58A364 + [epd] * 4 + [subp]`, `[subp] < 4`.  

        - `wwrite_epd`(epd, subp, value)  
        - `bwrite_epd`(epd, subp, value)  

            Writes a word/byte value to local memory address `0x58A364 + [epd] * 4 + [subp]`, `[subp] < 4`.  

        - `maskread_epd`(epd, mask) : EUDVariable  
            Uses [mask] as a mask to read the dword value at local memory address `0x58A364 + [epd] * 4`.  

        Example

        ```JavaScript
        // Much like the read/write example, the _epd family of functions differs from the memory offset reference, and the EPD function can be used to convert a memory address into an epd offset  
        function SetPlayerSupply(player: TrgPlayer, race, type, amount) {
            dwwrite_epd(EPD(0x582144) + (race) * 36 + (type) * 12 + (player), amount);
        }
        function GetPlayerSupply(player: TrgPlayer, race, type) {
            return dwread_epd(EPD(0x582144) + (race) * 36 + (type) * 12 + (player));
        }
        const oe, os = div(EncodeWeapon("C-10 Concussion Rifle"), 4);
        println("bread_epd Ghost weapon interval {}", bread_epd(EPD(0x656FB8) + oe, os));
        println("maskread_epd Ghost weapon interval {}", bitrshift(maskread_epd(EPD(0x656FB8) + 1 + oe, 0xFF000000), 24));
        bwrite_epd(EPD(0x656FB8) + oe, os, 1); // Modify Ghost weapon attack interval to 1
        ```

    <br />

    - #### **add_epd/subtract_epd**

        - `dwadd_epd`(epd, value)  
            Increments the dword value at local memory address `0x58A364 + [epd] * 4` by [value].  

        - `dwsubtract_epd`(epd, value)  
            Decrements the dword value at local memory address `0x58A364 + [epd] * 4` by [value].  

        - `wadd_epd`(epd, subp, value)  
        - `badd_epd`(epd, subp, value)  

            Increments the word/byte value at local memory address `0x58A364 + [epd] * 4 + [subp]` by [value], `[subp] < 4`.  

        - `wsubtract_epd`(epd, subp, value)  
        - `bsubtract_epd`(epd, subp, value)  

            Decrements the word/byte value at local memory address `0x58A364 + [epd] * 4 + [subp]` by [value], `[subp] < 4`.  

    <br />

    - #### **repmovsd_epd**

        - `repmovsd_epd`(dstepdp, srcepdp, copydwn)  
            Copies `[copydwn] * 4` bytes of content from local memory address `0x58A364 + [srcepdp] * 4` to memory address `0x58A364 + [dstepdp] * 4`.   

        Example

        ```JavaScript
        const src = Db(b"___1___2___3___4___5");
        const dst = Db(20);
        repmovsd_epd(EPD(src), EPD(dst), 5);
        // dst will be Db(b"___1___2___3___4___5")
        ```

    <br />

    - #### **dwepdread_epd**

        - `dwepdread_epd`(epd) : py_tuple[EUDVariable, EUDVariable]  
            Reads a pointer from local memory address `0x58A364 + [epd] * 4` and returns the pointer and its EPD value.  

        - `epdread_epd`(epd) : EUDVariable  
            Reads a pointer from local memory address `0x58A364 + [epd] * 4` and returns its EPD value.  

        Example

        ```JavaScript
        // Create a Marine and get its pointer and EPD value
        CreateUnit(1, "Terran Marine", $L("Location 1"), P1);
        const lastUnitEPD = EPD(0x628438);
        const ptr1, epd1 = dwepdread_epd(lastUnitEPD);
        var epd2 = epdread_epd(lastUnitEPD);
        ```

    <br />

    - #### **cunitread_epd**

        - `cunitread_epd`(epd) : EUDVariable  
            Reads a cunit pointer from local memory address `0x58A364 + [epd] * 4`. This function is optimized for reading cunit pointers and returns a pointer.  

        - `cunitepdread_epd`(epd) : py_tuple[EUDVariable, EUDVariable]  
            Reads a cunit pointer from local memory address `0x58A364 + [epd] * 4`. This function is optimized for reading cunit pointers and returns the pointer and its EPD value.  

        Example

        ```JavaScript
        // Create a Marine and get its pointer and EPD value
        CreateUnit(1, "Terran Marine", $L("Location 1"), P1);
        const lastUnitEPD = EPD(0x628438);
        const ptr1, epd1 = cunitepdread_epd(lastUnitEPD);
        var ptr2 = cunitread_epd(lastUnitEPD);
        ```

    <br />

    - #### **posread_epd**

        - `posread_epd`(epd) : py_tuple[EUDVariable, EUDVariable]  
            Reads a pos (location) from local memory address `0x58A364 + [epd] * 4`.  

        Example

        ```JavaScript
        const screenTilePosEPD = EPD(0x57F1D0);
        const x, y = posread_epd(screenTilePosEPD);
        println("The current screen coordinates on the map: ({}, {})", x, y);
        ```

    <br />

    - #### **_cp Series**

        - `dwread_cp`(cpoffset) : EUDVariable  
        - `dwwrite_cp`(cpoffset, value)  
        - `dwadd_cp`(cpoffset, value)  
        - `dwsubtract_cp`(cpoffset, value)  
        - `wread_cp`(cpoffset, subp) : EUDVariable  
        - `bread_cp`(cpoffset, subp) : EUDVariable  
        - `wwrite_cp`(cpoffset, subp, w)  
        - `bwrite_cp`(cpoffset, subp, b)  
        - `maskread_cp`(cpoffset, mask) : EUDVariable  
        - `maskwrite_cp`(cpoffset, mask, value)  
        - `dwepdread_cp`(cpoffset) : py_tuple[EUDVariable, EUDVariable]  
        - `epdread_cp`(cpoffset) : EUDVariable  
        - `cunitread_cp`(cpoffset) : EUDVariable  
        - `cunitepdread_cp`(cpoffset) : py_tuple[EUDVariable, EUDVariable]  
        - `posread_cp`(cpoffset) : py_tuple[EUDVariable, EUDVariable]  
        
        The usage of all functions in the _cp series can refer to the _epd series. The _cp series will use `Current Player + [cpoffset]` as epd.  
        They are usually used to improve code running efficiency and reduce the final number of triggers generated.  

        Example

        ```JavaScript
        // The following code is just to demonstrate the usage of _cp, not to improve efficiency. To improve efficiency, you may need to think for yourself.
        const screenTilePosEPD = EPD(0x57F1D0);

        setcurpl(screenTilePosEPD); // Set Current Player to screenTilePosEPD
        const x, y = posread_cp(0); // Read the value at the relative offset 0 bytes from Current Player, which actually reads the value at screenTilePosEPD

        setcurpl(P1); // Set Current Player to P1 to output information to Player 1
        println("Current screen coordinates on the map: ({}, {})", x, y);
        ```

    <br />

    - #### **readgen**

        - `readgen_epd`(mask, args) : duck  
        - `readgen_cp`(mask, args) : duck  

            Can be used to create custom local memory read functions.  

        Example

        ```JavaScript
        // 256 grids = 8192 pixels = x and y are within 0 ~ 8191 (0x1FFF)
        // Compile-time functions can only be defined using py_eval
        const posread_epd = readgen_epd(
            0x1FFF1FFF,
            list(0, py_eval('lambda x: x if x < 65536 else 0')),
            list(0, py_eval('lambda y: y // 65536 if y >= 65536 else 0')),
        );
        const x, y = posread_epd(epd_address);
        ```

    <br />

    - #### **memcpy**

        - `memcpy`(dst, src, copylen)  
            Copies [copylen] bytes of content from local memory address [src] to memory address [dst].  

    <br />

    - #### **memcmp**

        - `memcmp`(buf1, buf2, count) : EUDVariable  
            Compares [count] bytes of content between local [buf1] and [buf2] memory blocks.  
            If the two memory blocks are exactly the same, returns 0.  
            Otherwise, compares the first different byte and returns a result greater than or less than 0.  

    <br />

    - #### **strcpy**

        - `strcpy`(dst, src)  
            Copies the string (terminated by `\x00`) from local memory address [src] to memory address [dst].  

    <br />

    - #### **strcmp**

        - `strcmp`(s1, s2) : EUDVariable  
            Compares the strings (terminated by \x00) between local [s1] and [s2] memory blocks.  
            If the two memory blocks are exactly the same, returns 0.  
            Otherwise, compares the first different byte and returns a result greater than or less than 0.  

    <br />

    - #### **strlen**

        - `strlen`(ptr) : EUDVariable  
            Gets the number of ASCII characters in the string (terminated by \x00) pointed to by the local pointer [ptr].  

        - `strlen_epd`(epd) : EUDVariable  
            Gets the number of ASCII characters in the string (terminated by \x00) pointed to by the local [epd] offset pointer.  

    <br />

    - #### **strnstr**

        - `strnstr`(ptr, substr, count) : EUDVariable  
            Searches for another string [substr] within the first [count] ASCII characters of the string pointed to by the local pointer [ptr].  
            Returns the pointer if found, otherwise returns 0.  

    <br />

    - #### **dbstr**

        - `dbstr_addstr`(dst, src) : EUDVariable  
            Copies the local string [src] to memory address [dst], returns address [dst] + strlen([src]).  

        - `dbstr_addstr_epd`(dst, srcepd) : EUDVariable  
            Copies the string at local memory address `0x58A364 + [srcepd] * 4` to memory address [dst], returns address [dst] + strlen_epd([srcepd]).  

        - `dbstr_adddw`(dst, number) : EUDVariable  
            Converts a numeric value to text output at local memory address [dst], returns address [dst] + strlen(itoa([number])).  

        - `dbstr_addptr`(dst, ptr) : EUDVariable  
            Converts a numeric value to hexadecimal digit text output at local memory address [dst], returns address [dst] + strlen(itox([number])).  

        - `dbstr_print`(dst, *args, EOS=true, encoding="UTF-8")  
            Combines multiple parameters [*args] into a string output at local memory address [dst].  
            Named parameter [EOS] specifies whether to append a string termination symbol at the end of the string, default true.  
            Named parameter [encoding] specifies the encoding, default UTF-8.  

        - `sprintf`(dst, format_string : py_str, *args, EOS=true, encoding="UTF-8")  
            Formats multiple parameters [*args] according to [format_string] and outputs them to local memory address [dst].  
            Named parameter [EOS] specifies whether to append a string termination symbol at the end of the string, default true.  
            Named parameter [encoding] specifies the encoding, default UTF-8.  

        Example

        ```JavaScript
        const s = Db(100);
        var addr = unProxy(s);
        addr = dbstr_addstr(addr, Db("0123"));
        addr = dbstr_adddw(addr, 4567);
        addr = dbstr_addptr(addr, 0x89ABCDEF);
        simpleprint(s); // 0123456789ABCDEF

        dbstr_print(s, "0123", 4567, hptr(0x89ABCDEF));
        simpleprint(s); // 0123456789ABCDEF

        sprintf(s, "{}{}{:x}", "0123", 4567, 0x89ABCDEF);
        simpleprint(s); // 0123456789ABCDEF
        ```

    <br />

    - #### **ptr2s/epd2s**

        - `ptr2s`(ptr) : Db*  
            Reads the string at local memory address [ptr], equivalent to using `{:s}` placeholder in formatted text.  

        - `epd2s`(epd) : Db*  
            Reads the string at local memory address `0x58A364 + [srcepd] * 4`, equivalent to using `{:t}` placeholder in formatted text.  

    <br />

    - #### **hptr**

        - `hptr`(value) : Db*  
            Converts [value] to hexadecimal output, equivalent to using `{:x}` placeholder in formatted text.  

        Example

        ```JavaScript
        println("{}, {}", 0xAABBCC, hptr(0xAABBCC)); // 11189196, 00AABBCC
        println("{}, {:x}", 0xAABBCC, 0xAABBCC);     // 11189196, 00AABBCC
        ```

    <br />

    - #### **gettextptr**

        - `gettextptr()` : EUDVariable  
            Gets the local screen text pointer for the next line displayed on the screen.  

    <br />

    - #### **dwpatch_epd**

        - `dwpatch_epd`(dstepd, value)  
            Patches the local memory address `0x58A364 + [dstepd] * 4` by [value].  

    <br />

    - #### **GetMapStringAddr**

        - `GetMapStringAddr`(strID : TrgString) : EUDVariable  
            Gets the memory address of a local map string or string ID [strID].  

        Example

        ```JavaScript
        // It supports using strings and IDs to get, the following usages are equivalent
        const addr = GetMapStringAddr(6);
        const addr = GetMapStringAddr("Force 3");
        ```

    <br />

    - #### **GetTBLAddr**

        - `GetTBLAddr`(TBLKey : StatText) : EUDVariable  
            Gets the memory address of a TBL table Key/ID [TBLKey].  

            > It is worth mentioning that the TBLKey string itself may not actually exist in memory.  
            > For example, there is no "Terran Siege Tank (Tank Mode)" string in memory.  
            > The string corresponding to the TBLKey "Terran Siege Tank (Tank Mode)" (located in the stat_txt.tbl string section) prints out as "Terran Siege Tank"  

        Example

        ```JavaScript
        // It supports using TBLKey or TBL ID to get, the following usages are equivalent
        const addr = GetTBLAddr(4);
        const addr = GetTBLAddr("Terran Goliath");
        const addr = wread(dwread_epd(EPD(0x6D1238)) + $B("Terran Goliath"));
        ```

    <br />

    - #### **settbl**

        - `settbl`(tblID : StatText, offset, *args, encoding="cp949")  
        - `settbl2`(tblID : StatText, offset, *args, encoding="cp949")  

            Sets the local memory string value of the specified [tblID] in the TBL table at offset [offset] to *args. The difference between settbl and settbl2 is that settbl will add an EOS character at the end of the set string, while settbl2 will not.

        - `settblf`(tblID : StatText, offset, format_string, *args, encoding="cp949")  
        - `settblf2`(tblID : StatText, offset, format_string, *args, encoding="cp949")  

            Sets the local memory string value of the specified [tblID] in the TBL table at offset [offset] to a formatted string. The difference between settblf and settblf2 is that settblf will add an EOS character at the end of the set string, while settblf2 will not.

      ```JavaScript
        // The following code is equivalent
        settbl("Terran Goliath", 1, "1234");
        settbl2("Terran Goliath", 1, "1234\0");
        dbstr_print(GetTBLAddr("Terran Goliath") + 1, "1234\0", EOS = false); // Rename Terran Goliath to T1234
        ```

    <br />
    <br />

- ### Math Functions

    <br />

    - #### **atan2**

        - `atan2`(y, x) : EUDVariable  
            Arctangent function of two arguments, returns the polar angle of the point (x, y), i.e. the angle with the x-axis.  

        - `atan2_256`(x, y) : EUDVariable  
            The difference from atan2 is that in processing angles, it divides a circumference into 256 equal parts, and the angle is in 256 degrees, not 360 degrees.  

        > StarCraft units use angles stored in one byte, so they use the 256 degree system.  
        > 0 degrees faces up, 0 to 256 increments clockwise.  
        > 64 degrees faces right, 128 degrees faces down, 192 degrees faces left.  

        > **Warning**  
        > In euddraft version 0.9.9.7 and earlier, atan2_256 uses the mathematical coordinate system.  
        > In euddraft version 0.9.9.8 and above, atan2_256 is changed to use the StarCraft coordinate system.  

        Example

        ```JavaScript
        function _0998_above() {
            static var is0998above = false;
            once is0998above = l2v(atan2_256(10, 10) >= 90);
            return is0998above;
        }

        function angleBetween_256(x1, y1, x2, y2) {
            if (_0998_above()) {
                return atan2_256(y2 - y1, x2 - x1);
            }
            return atan2_256(x2 - x1, y1 - y2);
        }

        println("The angle from (131, 33) to (765, 546) is {}", angleBetween_256(131, 33, 765, 546));
        ```

    <br />

    - #### **sqrt**

        - `sqrt`(x) : py_int | EUDVariable  
            Calculates the square root of [x].  

        Example

        ```JavaScript
        function distanceBetween(x1, y1, x2, y2) {
            const x = x2 - x1;
            const y = y2 - y1;
            return sqrt(x*x + y*y);
        }

        println("The distance from (131, 33) to (765, 546) is {}", distanceBetween(131, 33, 765, 546));
        ```

    <br />

    - #### **lengthdir**

        - `lengthdir`(length, angle) : tuple[EUDVariable, EUDVariable]  
            Calculates the coordinates of another point by traveling [length] distance from (0, 0) in the direction of [angle] degrees.  

        - `lengthdir_256`(length, angle) : tuple[EUDVariable, EUDVariable]  
            The difference from lengthdir is that in processing angles, it divides a circumference into 256 equal parts, and the angle is in 256 degrees, not 360 degrees.  

        > StarCraft units use angles stored in one byte, so they use the 256 degree system.  
        > 0 degrees faces up, 0 to 256 increments clockwise.  
        > 64 degrees faces right, 128 degrees faces down, 192 degrees faces left.  

        > **Warning**  
        > In euddraft version 0.9.9.7 and earlier, lengthdir_256 uses the mathematical coordinate system.  
        > In euddraft version 0.9.9.8 and above, lengthdir_256 is changed to use the StarCraft coordinate system.  

        Example

        ```JavaScript
        function _0998_above() {
            static var is0998above = false;
            once is0998above = l2v(atan2_256(10, 10) >= 90);
            return is0998above;
        }

        function polarProjection_256(x0, y0, length, angle) {
            var dx, dy;
            if (_0998_above()) {
                dx, dy = lengthdir_256(length, angle);
                return x0 + dx, y0 + dy;
            } else {
                dx, dy = lengthdir_256(length, 320 - angle);
                return x0 + dx, y0 - dy;
            }
        }

        const x, y = polarProjection_256(1264, 880, 888, 73);

        println("Traveling 888 distance from (1264, 880) in the direction of 73 degrees (256 degrees) arrives at ({}, {})", x, y);
        ```

        [Example: UsePosition/main.eps](../Example/UsePosition/README.md#maineps)  

    <br />

    - #### **pow**

        - `pow`(x, y) : py_int | EUDVariable  
            Calculates [x] to the power of [y]. If both arguments are compile-time constants, it can return a constant at compile time.  

        Example

        ```JavaScript
        println("2^10 = {}", pow(2, 10));
        ```

    <br />

    - #### **div**

        - `div`(a, b) : py_tuple[EUDVariable, EUDVariable]  
            Unsigned integer division [a] divided by [b], supports only positive integers, returns quotient and remainder.  

        - `div_towards_zero`(a, b) : py_tuple[EUDVariable, EUDVariable]  
            Added in euddraft 0.9.9.8. Signed integer division, calculates the quotient and remainder of (a ÷ b), rounding the quotient towards zero.  

        - `div_floor`(a, b) : py_tuple[EUDVariable, EUDVariable]  
            Added in euddraft 0.9.9.8. Signed integer division, calculates the quotient and remainder of (a ÷ b), rounding the quotient towards negative infinity.

        - `div_euclid`(a, b) : py_tuple[EUDVariable, EUDVariable]  
            Added in euddraft 0.9.9.8. Signed integer division, calculates the quotient and remainder of Euclidean division of a by b.  
            This computes the quotient such that `a = quotient * b + remainder`, and `0 <= remainder < abs(b)`.  
            In other words, the result is a ÷ b rounded to the quotient such that `a >= quotient * b`.  
            If `a > 0`, this is equal to round towards zero; if `a < 0`, this is equal to round towards +/- infinity (away from zero).  

        Example

        ```JavaScript
        var a, b, quotient, remainder;
        a, b = 17, 3;
        quotient, remainder = div(a, b);
        println("div(17, 3) returns {}, {}", quotient, remainder);                  // div(17, 3) returns 5, 2
        a, b = 17, -3;
        quotient, remainder = div_towards_zero(a, b);
        println("div_towards_zero(17, -3) returns -{}, {}", -quotient, remainder);  // div_towards_zero(17, -3) returns -5, 2
        quotient, remainder = div_floor(a, b);
        println("div_floor(17, -3) returns -{}, -{}", -quotient, -remainder);       // div_floor(17, -3) returns -6, -1
        quotient, remainder = div_euclid(a, b);
        println("div_euclid(17, -3) returns -{}, {}", -quotient, remainder);        // div_euclid(17, -3) returns -5, 2
        a, b = -17, -3;
        quotient, remainder = div_towards_zero(a, b);
        println("div_towards_zero(-17, -3) returns {}, -{}", quotient, -remainder); // div_towards_zero(-17, -3) returns 5, -2
        quotient, remainder = div_floor(a, b);
        println("div_floor(-17, -3) returns {}, -{}", quotient, -remainder);        // div_floor(-17, -3) returns 6, -1
        quotient, remainder = div_euclid(a, b);
        println("div_euclid(-17, -3) returns {}, {}", quotient, remainder);         // div_euclid(-17, -3) returns 6, 1
        ```

    <br />

    - #### **rand**

        - `rand()` : EUDVariable  
            Generates a random integer in the range of 0~0xFFFF.  

        - `dwrand()` : EUDVariable  
            Generates a random integer in the range of 0~0xFFFFFFFF.

        > **Note**
        > Do not use random functions in desync conditions.  

        Example

        ```JavaScript
        const r = rand();
        ```

    <br />

    - #### **seed**

        - `srand`(seed)  
            Sets the random seed to [seed].  

        - `getseed()` : EUDVariable  
            Gets the set random seed.  

        > **Note**
        > Do not use random functions in desync conditions.    

        Example

        ```JavaScript
        var seed = getseed();
        srand(seed + 1);
        ```

    <br />

    - #### **randomize**

        - `randomize()` : EUDVariable  
            Initializes the random seed.  

        > **Note**
        > Do not use random functions in desync conditions.    

        Example

        ```JavaScript
        function onPluginStart() {
            randomize();
        }
        ```

    <br />
    <br />

- ### Bitwise Operation Functions

    <br />

    - #### **bitand**

        - `bitand`(a, b) : py_int | EUDVariable  
            Bitwise AND operation [a] & [b]  

        Example

        ```JavaScript
        var a = 0b0011; // 3
        var b = 0b1100; // 12
        println("{}", bitand(a, b)); // 0 (binary 0b0000)
        ```

    <br />

    - #### **bitor**

        - `bitor`(a, b) : py_int | EUDVariable  
            Bitwise OR operation [a] | [b]  

        Example

        ```JavaScript
        var a = 0b0011; // 3
        var b = 0b1100; // 12
        println("{}", bitor(a, b)); // 15 (binary 0b1111)
        ```

    <br />

    - #### **bitnot**

        - `bitnot`(a) : py_int | EUDVariable  
            Bitwise NOT operation ~[a]  

        Example

        ```JavaScript
        var a = 0b0011; // 3
        var b = 0b1100; // 12
        println("{}, {}", bitnot(a), b); // 12, 12 (binary 0b1100, 0b1100)
        ```

    <br />

    - #### **bitxor**

        - `bitxor`(a, b) : py_int | EUDVariable  
            Bitwise XOR operation [a] ^ [b]  

        Example

        ```JavaScript
        var a = 0b0111; // 7
        var b = 0b1110; // 14
        println("{}", bitxor(a, b)); // 9 (binary 0b1001)
        ```

    <br />

    - #### **bitnand**

        - `bitnand`(a, b) : py_int | EUDVariable  
            Bitwise NAND operation ~([a] & [b])  

        Example

        ```JavaScript
        var a = 0b0011; // 3
        var b = 0b1100; // 12
        println("{}", bitnand(a, b)); // 15 (binary 0b1111)
        ```

    <br />

    - #### **bitnor**

        - `bitnor`(a, b) : py_int | EUDVariable  
            Bitwise NOR operation ~([a] | [b])  

        Example

        ```JavaScript
        var a = 0b0011; // 3
        var b = 0b1100; // 12
        println("{}", bitnor(a, b)); // 0 (binary 0b0000)
        ```

    <br />

    - #### **bitnxor**

        - `bitnxor`(a, b) : py_int | EUDVariable  
            Bitwise XNOR operation `~([a] ^ [b])`  

        Example

        ```JavaScript
        var a = 0b0111;
        var b = 0b1110;
        println("{}", bitnxor(a, b)); // 6 (binary 0b0110)
        ```

    <br />

    - #### **bitlshift**

        - `bitlshift`(a, b) : py_int | EUDVariable  
            Bitwise Left shift operation `[a] << [b]`  

        Example

        ```JavaScript
        var a = 0b0111; // 7
        var b = 1;
        println("{}", bitlshift(a, b)); // 14 (binary 0b1110)
        ```

    <br />

    - #### **bitrshift**

        - `bitrshift`(a, b) : py_int | EUDVariable  
            Bitwise Right shift operation [a] >> [b]  

        Example

        ```JavaScript
        var a = 0b0111; // 7
        var b = 1;
        println("{}", bitrshift(a, b)); // 3 (binary 0b0011)
        ```


    <br />
    <br />

- ### QueueGameCommand Functions

    Queue game command to packet queue.  

    Starcraft periodically broadcasts game packets to other player. Game packets are stored to queue, and this function add data to that queue, so that SC can broadcast it.
  
    The QueueGameCommand functions are all for the local player rather than the current player, and cannot be used for players not in the game or computer players.  

    > **Note**
    > If packet queue is full, this function fails. This behavior is silent
    > without any warning or error, since this behavior shouldn't happen in
    > common situations. So **Don't** use this function too much in a frame.

    <br />

    - #### **QueueGameCommand**

        - `QueueGameCommand`(data, size)  
            Adds a data packet of size [size] [data] to the local broadcast queue. All functions in this section are wrappers for sending specific data packets to this function.  

    <br />

    - #### **QueueGameCommand_MinimapPing**

        - `QueueGameCommand_MinimapPing`(xy)  
            Adds a data packet to the local broadcast queue to ping at coordinates [xy] on the minimap. The xy calculation method is x + y * 65536.  

        Example

        ```JavaScript
        // Ping at coordinates 1234, 2345
        QueueGameCommand_MinimapPing(1234 + 2345 * 65536);
        ```

    <br />

    - #### **QueueGameCommand_QueuedRightClick**

        - `QueueGameCommand_QueuedRightClick`(xy)  
            Adds a data packet to the local broadcast queue for a right click at coordinates [xy]. The xy calculation method is x + y * 65536.  

        Example

        ```JavaScript
        // Right click at coordinates 1234, 2345. If units are selected, they will move there.
        QueueGameCommand_QueuedRightClick(1234 + 2345 * 65536);
        ```

    <br />

    - #### **QueueGameCommand_Select**

        - `QueueGameCommand_Select`(n, ptrList: EUDArray)  
            Adds a data packet to the local broadcast queue to select some units. [n] is the number of units, [ptrList] is the cunit pointer list, not the epd list.  

            > **Note**
            > This only sends a "units selected" data packet locally, it does not actually select units on the local screen. It only tells other online players that the local player has selected these units. If RightClick data packets are sent immediately after, these units will move to the target location.  

        Example

        ```JavaScript
        const uar = EUDArray(12);
        if (playerexist(P1) && GetPlayerInfo(P1).type == 0x06) { // Check if player 1 is an online human player
            foreach(i : py_range(3)) {
                uar[i] = dwread_epd(EPD(0x628438));
                CreateUnitWithProperties(1, "Zerg Overlord", "Location 1", P1, UnitProperty(invincible = true));
            }
        }
        if (getuserplayerid() == $P1) { // Check if the local player is player 1
            QueueGameCommand_Select(3, uar);
            QueueGameCommand_QueuedRightClick(1234 + 2345 * 65536);
        }
        ```

    <br />

    - #### **QueueGameCommand_PauseGame**

        - `QueueGameCommand_PauseGame()`  
            Adds a pause game data packet to the local broadcast queue.  

    <br />

    - #### **QueueGameCommand_ResumeGame**

        - `QueueGameCommand_ResumeGame()`  
            Adds a resume game data packet to the local broadcast queue.  

    <br />

    - #### **QueueGameCommand_RestartGame**

        - `QueueGameCommand_RestartGame()`  
            Adds a restart game data packet to the local broadcast queue.  

    <br />

    - #### **QueueGameCommand_UseCheat**

        - `QueueGameCommand_UseCheat`(cheats)  
            Use [cheats] locally, invalid for multiplayer games.  

        <details>

        <summary>Cheat code list</summary>

        ```js
        0x00000001 Black Sheep Wall
        0x00000002 Operation CWAL
        0x00000004 Power Overwhelming
        0x00000008 Something For Nothing
        0x00000010 Show me the Money
        0x00000020
        0x00000040 Game Over Man
        0x00000080 There is no Cow Level
        0x00000100 Staying Alive
        0x00000200 Ophelia
        0x00000400
        0x00000800 The Gathering
        0x00001000 Medieval Man
        0x00002000 Modify the Phase Variance
        0x00004000 War Aint What It Used To Be
        0x00008000
        0x00010000
        0x00020000 Food For Thought
        0x00040000 Whats Mine Is Mine
        0x00080000 Breathe Deep
        0x20000000 Noglues
        ```
        </details>

        Example

        ```JavaScript
        QueueGameCommand_UseCheat(0x00000001 | 0x00000002 | 0x00000010);  // Enable Black Sheep Wall + Operation CWAL + Show me the Money
        QueueGameCommand_UseCheat(0x00000002);                            // Disable Operation CWAL
        QueueGameCommand_UseCheat(0);                                     // Disable all cheats
        ```

    <br />

    - #### **QueueGameCommand_TrainUnit**

        - `QueueGameCommand_TrainUnit`(unit: TrgUnit)  
            Adds a train specified unitType data packet to the local broadcast queue. Use with QueueGameCommand_Select to select units.  

        Example

        ```JavaScript
        once {
            const uar = EUDArray(12);
            if (playerexist(P1) && GetPlayerInfo(P1).type == 0x06) { // Check if player 1 is an online human player
                SetResources(P1, Add, 10000, OreAndGas);
                uar[0] = dwread_epd(EPD(0x628438));
                CreateUnitWithProperties(1, "Terran Command Center", "Location 1", P1, UnitProperty(invincible = true));
            }
            if (getuserplayerid() == $P1) { // Check if the local player is player 1
                QueueGameCommand_Select(1, uar); // Check if the local player is player 1
                QueueGameCommand_QueuedRightClick(1234 + 2345 * 65536); /* Set the rally point to 1234, 2345 */
                QueueGameCommand_TrainUnit("Terran SCV"); /* Train an SCV */
            }
        }
        ```

    <br />

    - #### **QueueGameCommand_MergeDarkArchon**

        - `QueueGameCommand_MergeDarkArchon()`  
            Adds a merge dark archon data packet to the local broadcast queue. Use with QueueGameCommand_Select to select units.  

        Example

        ```JavaScript
        once {
            const uar = EUDArray(12);
            if (playerexist(P1) && GetPlayerInfo(P1).type == 0x06) { // Check if player 1 is an online human player
                foreach(i : py_range(6)) {
                    uar[i] = dwread_epd(EPD(0x628438));
                    CreateUnitWithProperties(1, "Protoss Dark Templar", "Location 1", P1, UnitProperty(invincible = true));
                }
            }
            if (getuserplayerid() == $P1) { // Check if the local player is player 1
                QueueGameCommand_Select(6, uar);
                QueueGameCommand_MergeDarkArchon();
            }
        }
        ```

    <br />

    - #### **QueueGameCommand_MergeArchon**

        - `QueueGameCommand_MergeArchon()`  
            Adds a merge archon data packet to the local broadcast queue. Use with QueueGameCommand_Select to select units.  

        Example

        ```JavaScript
        once {
            const uar = EUDArray(12);
            if (playerexist(P1) && GetPlayerInfo(P1).type == 0x06) { // Check if player 1 is an online human player
                foreach(i : py_range(6)) {
                    uar[i] = dwread_epd(EPD(0x628438));
                    CreateUnitWithProperties(1, "Protoss High Templar", "Location 1", P1, UnitProperty(invincible = true));
                }
            }
            if (getuserplayerid() == $P1) { // Check if the local player is player 1
                QueueGameCommand_Select(6, uar);
                QueueGameCommand_MergeArchon();
            }
        }
        ```


---


# epScript Reference

<br />

- Language Reference
    - [Syntax](Syntax.md)  
    - [Use Of Variables](Use-of-Variables.md)  
    - [Use Of Functions](Use-of-Functions.md)  
    - [Use Of Objects](Use-of-Objects.md)  
    - [Understanding Strings](Understanding-Strings.md)  
    - [Built-in Object Types](Built-in-Object-Types.md)  
    - [Built-in Object Types Ext](Built-in-Object-Types-Ext.md)  
    - [Constants Reference](Constants-Reference/Constants-Reference.md)  
    - [Built-in Functions](Built-in-Functions.md) 
- Description
    - [Getting Started](#getting-started)
        - [Environment Preparation](#environment-preparation)
        - [Map Preparation](#map-preparation)
        - [New Project](#new-project)
        - [Example Projects](#example-projects)
    - [Running Mode](#running-mode)
        - [Script File Extension Differences](#script-file-extension-differences)
        - [Load Order](#load-order)
    - [The Difference Between .edd And .eds](#the-difference-between-edd-and-eds)
        - [For .edd Format](#for-edd-format)
        - [For .eds Format](#for-eds-format)
    - [Data Synchronization](#data-synchronization)
    - [Game Time](#game-time)
        - [Game Frame](#game-frame-fr)
        - [Game Seconds](#game-seconds)
        - [Game Speed](#game-speed)
        - [Triggers Poll Interval](#triggers-poll-interval)
    - [Current Player And Local Player](#current-player-and-local-player)
        - [Current Player](#current-player)
        - [Local Player](#local-player)

<br />

## Getting Started 
If there are any parts you don't understand, you can try searching the Internet to solve them.  

Here we assume you already know how to use ScmDraft2 for basic terrain design.  
- If not, refer to: [SCMD](http://www.stormcoast-fortress.net/Irregularies/#downloads)   

Here we assume you already have a basic understanding of EUD.   
- If not, refer to: [What is EUD](What-is-EUD.md)  

### Environment Preparation

Prepare a Windows 10 or higher PC, or a virtual machine.  
Prepare ScmDraft2. If not already prepared, look back a few lines.  

- Download [euddraft0.9.9.9.zip](https://github.com/armoha/euddraft/releases/download/v0.9.9.9/euddraft0.9.9.9.zip)   
    Unpack euddraft to a path with only English letters and no spaces, e.g. D:\SCRMapDevTools\euddraft0.9.9.9 
- Download [VSCode](https://code.visualstudio.com/Download)  
    Install it, install it however you like.   
    Install the eps-server plugin from the VSCode plugin store.  

- Open file extension display in your operating system.   
    For Windows 10, refer to [https://www.google.com/search?q=Open-file-extension-display-in-windows-10](https://www.google.com/search?q=Open+file+extension+display+in+windows+10)   
    For Windows 11, refer to [https://www.google.com/search?q=Open-file-extension-display-in-windows-11](https://www.google.com/search?q=Open+file+extension+display+in+windows+11)  


### Map Preparation  

Prepare a normal map file, you can create a new one with ScmDraft2 and then save it as Starcraft: Remastered Broodwar Map (*.scx) format.   
Also save it to a path with only English letters and no spaces, e.g. D:\Projects\test\basemap.scx.  


### New Project
1. Create a new text document and change its extension to edd, e.g. D:\Projects\test\test.edd  
    Open this edd file with VSCode (just drag the file into the open VSCode window).  
Then change its content to:  
    ```MakeFile
    [main]
    input: basemap.scx
    output: test.scx

    [main.eps]
    ```
    The above code uses relative paths as an example, it actually supports absolute paths.   

2. Create a new text document and change its extension to eps, e.g. D:\Projects\test\main.eps  
    Open this eps file with VSCode.  
    Then change its content to:  
    ```JavaScript
    function onPluginStart() { // This function will be executed once when the game starts
        DisplayTextAll("Hello World");
    }

    function beforeTriggerExec() { // This function will be executed once each frame before classical triggers

    }

    function afterTriggerExec() { // This function will be executed once per frame after classical triggers

    }
    ```

3. Create a new text document and change its extension to bat, e.g. D:\Projects\test\build.bat  
    Open this bat file with VSCode and change its content to:  
    ```PowerShell
    D:\SCRMapDevTools\euddraft0.9.9.9\euddraft.exe test.edd
    ```
    The above code assumes you unpacked euddraft to D:\SCRMapDevTools\euddraft0.9.9.9. If not, you should replace it.  

    Now the project is ready. Just double click to run build.bat to generate test.scx. Put this map in the map directory of StarCraft: Remastered. Then when you enter the game, you will see `Hello World` output on the screen.


### Example Projects

- If you really don't understand the configuration process above, you can choose a simple example project to view:  
    - [Trigger-and-RawTrigger](../Example/Trigger-and-RawTrigger/README.md)
    - [ChangeSupplyLimit](../Example/ChangeSupplyLimit/README.md)
    - [UsePosition](../Example/UsePosition/README.md)
    - [\[MSQC\]GameSpeedTextMenu](../Example/%5BMSQC%5DGameSpeedTextMenu/README.md)  

<br /><br />



## Running Mode

### Script File Extension Differences
- If it is a `.py` format script, the extension name can be omitted in the .eds/.edd file. `.eps` format scripts need to add the extension name.  

    ```ini
    [main]
    input: basemap.scx
    output: outputmap.scx

    [eudTurbo]
    :: It actually loads a script named eudTurbo.py

    [main.eps]
    :: Load it like this if it is .eps format
    ```

### Load Order

- The order of plugin names in the configuration file is associated with their loading order after the game starts. After the game starts, onPluginStart() in the script will be executed once, and beforeTriggerExec(), triggers, and afterTriggerExec() will be executed cyclically on all players' machines.  

    For example, with the following main.edd configuration:  

    ```ini
    [main]
    input: in.scx
    output: out.scx

    [eudTurbo]
    [a.eps]
    [b.eps]

    ```

    The execution order after the game starts is:  

    ```PowerShell
    eudTurbo.onPluginStart()
    a.onPluginStart()
    b.onPluginStart()
    Executed cyclically every frame:
        eudTurbo.beforeTriggerExec()
        a.beforeTriggerExec()
        b.beforeTriggerExec()
        SCMD triggers
        b.afterTriggerExec()
        a.afterTriggerExec()
        eudTurbo.afterTriggerExec()
    ```
    <br />

## The Difference Between .edd And .eds

euddraft handles these two extensions differently.

- ### For .edd Format  

    After successfully compiling and generating the map, it will keep waiting. If the files in the project directory change, it will automatically recompile and generate the map again.  
    If unsuccessful, it will output error messages. You can press R to recompile and generate after modifying.  

- ### For .eds Format  

    After successfully compiling and generating the map, it will exit.   
    If unsuccessful, it will output error messages and wait for you to press Enter to exit.  <br /><br />


## Data Synchronization

If you assign `desync-data` (such as the player's current mouse position) to a variable, the value of the variable will be different for each player's machine. If you execute an action that requires `sync-data` (such as creating a unit) based on the state of that variable, it may cause the `sync-data` to be out of sync for players in multiplayer games (e.g. a unit is created on player A's machine but not on player B's machine), leading to a drop.  

Such tasks can usually be assisted by the MSQC plugin.  

<!-- [Example: GameSpeedTextMenu](res/%5BMSQC%5DGameSpeedTextMenu/)   -->
<br /><br />



## Game Time 

The game time in StarCraft 1 is different from real time.  

- ### Game Frame (fr) 

    The minimum unit of game time in StarCraft is the game frame (fr):  
    `1 fr` == `1/16 game seconds`

- ### Game Seconds 

    The formula for converting game seconds and game frames in StarCraft:  
    `1 game seconds` == `16 fr`

- ### Game Speed 
    StarCraft has seven standard game speeds.  
    At different game speeds, the system time represented by each game frame is different.  
    System time is usually equal to real world time.  
    <details>
    
    <summary>For each game frame, the corresponding system time (accurate value, not approximate) with no network latency</summary>

    ```JavaScript
    Slowest: 1 fr == 0.167 system seconds  
    Slower : 1 fr == 0.111 system seconds
    Slow   : 1 fr == 0.083 system seconds 
    Normal : 1 fr == 0.067 system seconds
    Fast   : 1 fr == 0.056 system seconds   
    Faster : 1 fr == 0.048 system seconds
    Fastest: 1 fr == 0.042 system seconds
    ```
    </details>

    So at the Fastest game speed, 1 game second is `0.042 × 16 = 0.672` real seconds, and 1 system second is `1 ÷ 0.042 ÷ 16 ≈ 1.488` game seconds.  

- ### Triggers Poll Interval

    Triggers in StarCraft are single-threaded polling.  
    Without using eudTurbo and Wait actions, the trigger polling interval is `31 fr`, which is `1.9375 game seconds`.  
    The first poll after the game starts is at `2 fr`, which is `0.125` game seconds.  

    <details>
    
    <summary>Trigger polling times after the game starts</summary>

    ```JavaScript
    First   poll at   2 game frames,  0.1250 game seconds
    Second  poll at  33 game frames,  2.0625 game seconds
    Third   poll at  64 game frames,  4.0000 game seconds
    Fourth  poll at  95 game frames,  5.9375 game seconds
    Fifth   poll at 126 game frames,  7.8750 game seconds
    Sixth   poll at 157 game frames,  9.8125 game seconds
    Seventh poll at 188 game frames, 11.7500 game seconds
    Eighth  poll at 219 game frames, 13.6875 game seconds
    Ninth   poll at 250 game frames, 15.6250 game seconds
                    ...And so on...
    ```
    </details>
    
    The game seconds comparsion in the ElapsedTime condition parameter takes the integer part.
    ```JavaScript
    function beforeTriggerExec() {
        if (ElapsedTime(Exactly, 6)) {
            DisplayTextAll("This message will not output");
        }
    }
    ```
    So this condition will not be met, because the fourth poll is at 5.9375 game seconds with an integer part of 5, and the fifth poll is at 7.8750 game seconds with an integer part of 7, so ElapsedTime(Exactly, 6) will never be true.  
    If you want to execute an action once after 6 game seconds, you can write like this:  
    ```JavaScript
    function beforeTriggerExec() {
        once (ElapsedTime(AtLeast, 6)) {
            DisplayTextAll("This message will output once after 6 game seconds");
        }
    }
    ```
    Similarly, the CountdownTimer condition also takes the integer part of the countdown at the top of the screen.     
    Therefore, when writing conditions related to time comparsion, Exactly (`==`) should not be used, but AtLeast (`>=`) or AtMost (`<=`) should be used.  <br /><br />


## Current Player And Local Player

`Current Player` and `Local Player` are two different concepts.

### Current Player 

The `Current Player` is a global variable. In some trigger actions, `Current Player` is used as an execution parameter.  
Some trigger conditions and actions support passing a `Player` parameter, then, you can set the `Player` parameter to `13` to use the `Current Player` global variable as its parameter.  
The value of the `Current Player` global variable does not necessarily have to be any player's ID, it can store any integer value.  

<details>
    
    <summary>Actions that only take effect on machines where Current Player == Local Player (allow desync use, can be used individually on some player machines)</summary>

- DisplayText  
- CenterView  
- PlayWAV  
- MinimapPing  
- TalkingPortrait  
- Transmission  
- SetMissionObjectives  
</details>

<details>
    
    <summary>Actions that only take effect on Current Player (must be used synchronously on all player machines, otherwise disconnected)</summary>

- SetAllianceStatus  
- RunAIScript  
- RunAIScriptAt  
- Draw  
- Defeat  
- Victory  
</details>

The `setcurpl` function can be used to set the value of the `Current Player` global variable.  
The `getcurpl` function can be used to get the current value of the `Current Player` global variable.  
No matter what value you set for the `Current Player`, the code will execute on all players' machines.  

```PHP
setcurpl(P1);
DisplayText("Printed content for player 1");
setcurpl(P2);
DisplayText("Printed content for player 2");
setcurpl(P3);
DisplayText("Printed content for player 3");

// $CurrentPlayer is the constant number 13. It can cause some player-related conditions or actions to access the current player value  
// $CurrentPlayer != getcurpl()  
if ($CurrentPlayer == 13) {
    DisplayTextAll("Well, right");
}

// Set Fastest game speed x2
setcurpl(-122787 + 6);
SetDeaths($CurrentPlayer, SetTo, 21, 0);
```

### Local Player 

getuserplayerid() can be used to get the local player ID. It returns a different value for each machine and is unrelated to the value set by setcurpl.   
The ability to use getuserplayerid() to get the local player ID means you can decide at runtime whether or not to execute certain code on the local machine.   
It helps improve performance. When there are many players, not all code needs to execute for each player, e.g. no need to generate text prompts for all players for each player.  
Of course, if you pollute sync-data directly or indirectly due to unfamiliarity with synchronization rules using getuserplayerid(), it can also lead to data synchronization causing dropped

```JavaScript
setcurpl(P1);
println("Current player ID: {}", getuserplayerid());
setcurpl(P2);
println("Current player ID: {}", getuserplayerid());
setcurpl(P3);
println("Current player ID: {}", getuserplayerid());
```

    

  

