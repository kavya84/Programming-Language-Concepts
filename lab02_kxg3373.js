//Name : KAVYA SRI GARIKIPATI
//STUDENT ID : 1001953373
//Due Date : 03/07/2023


// 1st Answer
console.log('Answer 1:')  //printing Answer 1
var inputtable = [1,2,3,4,5,6,7,8,9,10]; //creating an array named as inputtable which has numbers between 1 and 10
console.log('The array which has numbers between 1 and 10 is ' +inputtable); //displaying the result
//---------------###################################################################################################---------------------------------------------------
//2nd Answer
//2a) Answer
console.log('Answer 2:') //printing Answer 2
//Here the components in inputtable is not more than 10 and also 5*10=50 is not greater than 51 but 5*11=55
//We are utilizing inputtable to find the products of 5 i.e from 5 to 50.
var fiveTable = []; //naming the variable as 'fiveTable'
function five_multiples(y){//the function which is taking the primary inputtable element's list as a parameter
    if(y==10) //After final component in inputtable, it should stop
    {
        return 0;
    }
    else{ //Inside 1 to 10
        fiveTable[y]= inputtable[y] * 5;//Taking numerous of 5 into array which is in our run
        five_multiples(y+1);//function is called for upcoming element
    }
}
five_multiples(0);
console.log('2a): set of multiples of 5 between 1 and 51 are '+fiveTable);//result is getting displayed
//----------------------------------------------------------------------------------
//2b) answer
var thirteenTable = []; //creating the variable thirteenTable
//Hence elements in inputtable are not more prominent than 10 and 13*10=130 is also not more prominent than 131 , but 13*11=143, therefore we can use inputtable to find the products of 13 from 1 to 131
function thirteen_multiples(y){//This function takes the primary inputtable element's list as the parameter
    if(y==10){//Inputtable's final component must halt
        return 0;
    }
    else //inside 1 to 10
    {
        thirteenTable[y] = inputtable[y] * 13;//Taking away a different of 13 into the array that is present in inputtable
        thirteen_multiples(y+1);// function is called for the respective element
    }
}
thirteen_multiples(0);
console.log('2b) : Set of multiples of 13 between 1 and 131 are '+thirteenTable);//displaying the result
//--------------------------------------------------------------------------------
//2c) answer
var squaresTable = []; //declaring the variable squaresTable
function squares_multiples(y){//This function takes the primary inputtable element's list as the parameter
    if(y==10){//Inputtable's final component must halt
        return 0;
    }
    else{
        squaresTable[y] = inputtable[y]*inputtable[y];//computing squares and placing them within the array
        squares_multiples(y+1);//function is getting called for other component
    }
} 
squares_multiples(0);
console.log('2c) : Set of squares of the numbers in inputtable are '+squaresTable);//Printing the result
//-----------------------#################################################################################--------------------------------------------------------
// 3rd Answer
console.log('Answer 3:')
console.log('LISTING THE ODD MULTIPLES OF 5');//Printing the odd multiples of 5
var k = 1;
function oddMultiples_of_5(numbers)//this function takes 5's multiplier as the parameter
{
    if(5*numbers > 100)//if it is greater than 100, that means it is out of our run and it should stop
    {
        return 0;
    }
    if(numbers%2 == 1)//product is odd as the numbers are odd(because odd*odd=odd)
    {
        console.log(k+' odd multiple of five : '+5*numbers);//Display the odd multiples of 5
        k=k+1;//increment
    }
    oddMultiples_of_5(numbers+1);//function is called for another multiplier
}
oddMultiples_of_5(1);//We are starting with 1 to remain within the extend of 1 to 100 
//------------####################################################################################################-------------------------------------------------
//4th Answer
// the sum of even multiples of 7 between 1 and 100.
// -------- 0+14+0+28+0+42+.......+98 = 392 ---------
console.log('Answer 4:') //printing Answer 4:
var output = 0;//declaring output variable
function sum_of_even_multiplesOf_seven(numbers){//this function takes 7's multiplier as a parameter
    if(7*numbers>100)//It is greater than 100 , out of our run and must stop
    {
        return 0;
    }
    if(numbers%2 == 1){//product becomes odd , since multiplier is odd(because odd*odd=odd)
        return 0 + sum_of_even_multiplesOf_seven(numbers+1); //Because the item is odd, we are including the function call for the respective multiplier
    }
    if(numbers%2 == 0){//product will become even since multiplier is even(because odd*even=even)
        output = (7*numbers) + sum_of_even_multiplesOf_seven(numbers+1);//because the product is even , we should add it to the function call of the next multiplier
        return output;
    }
}
sum_of_even_multiplesOf_seven(1);//starting with 1 to remain within the extend of 1 to 100
console.log(' the sum of even multiples of 7 between 1 and 100 is '+output);//printing the result here
//------------############################################################################################################--------------------------------------------
//5th Answer
//we use currying work - Currying in utilitarian programming refers to the transformation of a function with various arguments into a series of nesting functions. It gives back a contemporary function that takes the next argument inline into account.
console.log('Answer 5:') //printing Answer 5:
function cylinder_volume(r){//this is changed because of the work given into a nested function which has single arguments using currying, to start with we consider radius as the input
    return (h) => {//considering tallness as the input as a second argument within the nested function
        return 3.14*r*r*h;//returning the volume of the cylinder as there are no inputs which are cleared out
    }
}
console.log('5a: Volume of a cylinder when h=10 and r=5 is '+cylinder_volume(5)(10));//calling function for the cylinder with r=5 and h=10
console.log('5b: Volume of a cylinder when h=17 and r=5 is '+cylinder_volume(5)(17));//calling function for the cylinder with r=5 and h=17
console.log('5c: Volume of a cylinder when h=11 and r=5 is '+cylinder_volume(5)(11));//calling the function for the cylinder with r=5 and h=11
//---------------------#####################################################################################################-----------------------------------------------------
//6th Answer
console.log('Answer 6:') //printing Answer 6:
console.log('HTML table consisting of a table row and 2 table cells as shown here')//show an HTML table consisting of a table row that has at least one table cell/element.
makeTag = function(beginTag, endTag){ //Code which is given for us in the question
    return function(textcontent){
       return beginTag +textcontent +endTag;
    }
 }
 //displaying the yields by calling the function which uses currying
 console.log(makeTag("<",">")("table")); //prints "<table>"
 console.log(makeTag("<",">")("tr"));//prints "<tr>"
 console.log(makeTag("<",">")("th")+"Student ID"+makeTag("</",">")("th"));//displays "<StudentID>"
 console.log(makeTag("<",">")("th")+"Student Full Name"+makeTag("</",">")("th"));//displays "<Student Full Name>"
 console.log(makeTag("<",">")("th")+"Department"+makeTag("</",">")("th"));//displays "<Department>"
 console.log(makeTag("</",">")("tr"));//displays "</tr>"
 console.log(makeTag("<",">")("tr"));
 console.log(makeTag("<",">")("td")+1001953373+makeTag("</",">")("td"));//Student ID is getting displayed
 console.log(makeTag("<",">")("td")+"Kavya Sri Garikipati"+makeTag("</",">")("td"));//Student Name is getting displayed
 console.log(makeTag("<",">")("td")+"CSE"+makeTag("</",">")("td"));//Department is displayed
 console.log(makeTag("</",">")("tr"));
 console.log(makeTag("<",">")("tr"));
 console.log(makeTag("<",">")("td")+1001956789+makeTag("</",">")("td"));
 console.log(makeTag("<",">")("td")+"Akhila Kolapalli"+makeTag("</",">")("td"));
 console.log(makeTag("<",">")("td")+"DS"+makeTag("</",">")("td"));
 console.log(makeTag("</",">")("tr"));
 console.log(makeTag("</",">")("table"));
 //--------------------##############################################################################################################################-----------------------------------------------------------------------
 //7th Answer
 console.log('ANSWER 7 :')//printing Answer 7

function genericMulti(odd_even_nums,multiplicand,numbers){
    if(multiplicand*numbers>100){ //if it is greater than 100, it will be out of our extend , so it tends to stop
        return 0;//returns 0
    }
    if(odd_even_nums == 1){ //if the product is odd,we should go advance
        if(numbers%2==1){ //hence odd*odd=odd, we need to check the Multiplier
            console.log(multiplicand*numbers); //product value is displayed
        }
    }
    else{ //If the item is even, we will go advance
        if(numbers%2==0){ // hence odd*even=even, we check numbers value
         console.log(multiplicand*numbers);//displaying the product
        }
    }
    genericMulti(odd_even_nums,multiplicand,numbers+1); //calling the function for the another Multiplier
}

console.log('odd multiples of 5 using currying listed as below : ')//printing odd multiples of 5 using currying
genericMulti(1,5,1); //the odd multiples of 5 between 1 and 100
console.log('sum of even multiples of 7 using currying are : ') //Displaying sum of even multiples of 7
genericMulti(0,7,1); //Even multiples of 7 that are between 1 and 100
//---------------------------------###########################################################################################################-----------------------------------------------------
 //8th Answer
 console.log('Answer 8 :')//printing Answer 8
 console.log('(5 points) Following instructions')//prints following instructions
 //--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


