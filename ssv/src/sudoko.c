#include <stdio.h>

//Validating sudoko array's rows and columns
/*
This function takes a multidimesntion 9x9 array,
seperate it into rows and columns and check their repeated content.
*/
int chkOrthogonal(int array[9][9]){
    //Looping through parent array
    for(int i = 0; i < 9; i++) {
        //assigning temporary horizontal and vertical variables and arrays for rearranging rows and columns boxes  
        int temph = 0,tempv = 0,harray[9] = {0,0,0,0,0,0,0,0},varray[9] = {0,0,0,0,0,0,0,0};
        //looping through childern arrays
        for(int j = 0; j < 9; j++) {
            //validating boxes' content value range  
            if(array[i][j] > 9 || array[i][j] < 1){
                printf("Range from 1 -> 9.\n");
                //returning Zero means there is an error.
                return 0;
            }
        //seperating the sudoko array into rows and columns 
            harray[j] = array[i][j]; //horizontal array > row
            varray[j] = array[j][i]; //vertical array > column
        }
        //looping through rows to arrang their content and check the repeated value.
        for(int j = 0; j < 9; j++) {
            if(harray[j] > harray[j+1]){
                temph = harray[j];
                harray[j] = harray[j+1];
                harray[j+1] = (j+1 > 8) ? 0 : temph;
            }else if(harray[j] == harray[j+1]){
                printf("Check combination in the row %d. #%d repeated.\n",i+1,harray[j]);
                return 0;
            }
        //looping through columns to arrang their content and check the repeated value.            
            if(varray[j] > varray[j+1]){
                tempv = varray[j];
                varray[j] = varray[j+1];
                varray[j+1] = (j+1 > 8) ? 0 : tempv;
            }else if(varray[j] == varray[j+1]){
                printf("Check combination in the column %d. #%d repeated.\n",i+1,varray[j]);
                return 0;
            }
        }
    }
    //returning one means no error.
    return 1;
}

//Validating sudoko Block
/*
This function takes a start point, an end point, and an array
to loop through and get the block's content in a block array
*/
int chkBlock(int a,int b,int array[9][9]){
    int x = 0,temp = 0,barray[9] = {0,0,0,0,0,0,0,0};

    for(int i=a; i < a+3; i++) {
        for(int j=b; j < b+3; j++) {
            barray[x] = array[i][j];
            x++;
        }
        
    }
        //looping through the block to arrang its content and check the repeated value.            
        for(int z = 0; z < 9; z++) {
        if(barray[z] > barray[z+1]){
            temp = barray[z];
            barray[z] = barray[z+1];
            barray[z+1] =  (z+1 > 8) ? 0 : temp;
            
        }else if(barray[z] == barray[z+1]){
            printf("Check combination in the Block rows [ %d => %d ] - columns [ %d => %d ], #%d repeated.\n",a+1,a+4,b+1,b+4,barray[z]);            
            return 0;
        }

    }
    return 1;

}


/*
This function takes a multidimesntion 9x9 array,
seperate it into blocks and call chkBlock function to check block's repeated values.
*/
int chkBlocks(int array[9][9]){
    for(int i = 0; i < 9; i=i+3) {
        for(int j = 0; j < 9; j=j+3) {
            if(!chkBlock(i,j,array)){
                return 0;
            }
        }
    }
    return 1;
}

/*
Main function
-Prints application's guidelines and help text.
-Takes user input .
-Calls action function and read thier exist code. 
*/

int main () {
    char c;
//ASSIGNING ARRAY OF SUDOKO SOLUTION.
    int sudoko[9][9];

    printf("WELCOME TO SUDOKO SOLUTION CHECKER.\n");
    printf("TYPE 'f' TO ENTER THE SOLUTION ON A FILE.\n");
    printf("TYPE 'i' TO ENTER THE SOLUTION ON THE TERMINAL.\n");
    printf("TYPE 'e' TO EXIT.\n");
//INFINITE LOOP TO GET THE USER'S INPUT.
    while(1){
        printf("Please Enter [f/i/e] to continue >");
        scanf(" %c",&c);

        if(c == 'f'){
            //GETTING FILE CONTAINING THE SOLUTION.
            char path[100];
            printf("Please Enter the solution file path >");
            scanf("%s",&path);
            FILE *file;
            file=fopen(path, "r");
            int c;
            //CHECKING IF THE FILE IS OPENED
            if (file) {
                //GETTING THE FILE CONTENTS IN THE SUDOKO ARRAY
                 for(int i=0;i<9;i++)
                {
                    for(int j=0;j<9;j++)
                    {
                        c = fscanf(file,"%d ",&sudoko[i][j]);
                        if(c == EOF)
                            continue;
                    }
                }    
                //CLOSING THE FILE.
                fclose(file);
            }else{
                //FILE DOESNOT EXIST .. GETTING USER OPTION AGAIN.
                continue;
            }
            //SUDOKO ARRAY ASSIGNING WENT WELL, GETTING OUT OF THE LOOP.
            break;
        
        }else if(c == 'i'){
            printf("Please Enter the solution.\n");
            //GETTING SOLUTION FROM THE TERMINAL.
            for(int i=0;i<9;i++)
            {
                for(int j=0;j<9;j++)
                {
                    scanf(" %d",&sudoko[i][j]);
                }
            }
            //SUDOKO ARRAY ASSIGNING WENT WELL, GETTING OUT OF THE LOOP.        
            break;
        }else if(c == 'e'){
            return 1;
        }else {
        //WRONG OPTION .. GETTING USER OPTION AGAIN.
            continue;
        }

    }
      
    //CHECKING IF THE SOLUTION IS RIGHT. 
    (!chkOrthogonal(sudoko) || !chkBlocks(sudoko)) ? printf("WRONG SOLUTION \n") : printf("RIGHT SOLUTION \n");
    return 0;
}