# Data Types
* int, double, bool, char, string
* datetime: non-negative integers, UNIX time (seconds from 1970-01-01 00:00:00)
* color: non-negative integers, for example, white can be C'255,255,255' (literal), clrWhite (name), 0xFFFFFF (integrals)
* "u" for unsigned (positive): uint, ushort, ulong
* `NormalizeDouble(double, precision)`: useful to **prevent broker error** caused by invalid double precision
    * Note that it is not perfect, and it does not change the print output.
    * Use `DoubleToString(double, precision)` for print floating numbers.

# Variables
* `input` variables cannot be modified.
* `static` variables can be declared within functions, and their values peresist between function calls.
    * but the scope of static vairables are NOT global.
* constant is declared by `#define`
    * `#define PI 3.1415`
    * `#define AREA(pi, r) pi * r * r`
* enumarations
    * `enum ENUM_TOGGLE {ON, OFF};`
    * `ENUM_TOGGLE short_toggle;`

# Functions
* All functions are global – cannot declare functions within a function
* Use “&” in function declaration to pass by reference – use sparsely
* Print `__FUNCTION__` to identify part of the source code the message is coming from

# Boolean Expressions
* “&&” for AND, “||” for OR, “!” for NOT

# Mathematical Operations
* `bool MathIsValidNumber(x)`
* `int MathRound(x)` or simply `round(x)`
* `int MathFloor()`, `int MathCeil()`
* `MathMin(a, b)`, `MathMax(a, b)`
* `MathAbs(x)`
* `MathMod(x, y)` = x % y
* `MathPow(base, exponent)`
* `MathExp(x)`, `MathExpm1(x)` = MathExp(x) – 1
* `MathSqrt(x)`
* `MathLog(x)` = ln(x), `MathLog10(x)`, `MathLog1p(x)` = ln(1+x)
* Trigonometric:
    * `MathSin(rad)`, `MathCos(rad)`, `MathTan(rad)`
    * Inverse (Arc), Hyperbolic (h), Inverse Hyperbolic (Arc, h)

**zero dividion** will cause **critical error** - the program will be force-stopped
* remeber to check your divisor between divide by it!

# Random Number
* MathRand() yield a number from range [0, 32767]
    * One way to make it yield in a selected range is by using MathMod(dividend, divisor). The resulted range will be [0, divisor-1]
        * For example, to yield [0, 1]: `int random = MathMod(MathRand(), 2);`
        * Must do `void MathSrand(seed)` to select seed
            * Example of seed can be `TimeCurrent()`, `GetTickCount()`

# String Functions
* `bool StringAdd(&str, substr)`
* `int StringConcatenate(&str, substr1, substr2, ...)`: returns the number of chars in the string
* `int StringLen(str)`
* `string StringSubstr(str, int start_pos, int length)`: use -1 as length to copy the rest of the string
* `StringReplace(&str, string find, string replace)`: replace all instances of find

# Time Functions
* Server-based
    * `TimeCurrent()`: returns the last known server time (based on latest tick)
* Local-based (computer)
    * `TimeLocal()`: returns the local time
    * `TimeGMT()`: returns the time in GMT (based on local time)
    * `GetTickCount()`: returns the number of seconds elapsed since program (trading platform, not EA/script/indicator) start


