#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

struct Employee {
    string Name;
    int Id;
    int Mobile;
    int Age;
    string Address;
};

struct Product {
    string Name;
    int Id;
    string Description;
};

Product getProductInfo(){
    Product product;
    char c = 'n';
    cout << "Add New Product." <<endl;
    while(1){
        cout << "Enter The following information: " <<endl;
        cout << "Product Id: " ;
        if (!(cin >> product.Id)) {
            cout <<"Id should be a number\n\n"<<endl;
            cin.clear();
            cin.ignore(10000,'\n');
            continue;
        }

        cin.ignore();
        cout << "Product Name: ";
        getline(cin, product.Name);

        cout << "Product Description: " ;
        getline(cin, product.Description);

        cout << "Id: " << product.Id << ", Name: " << product.Name << ", Description: " << product.Description <<endl;
        cout << "correct information ? [y/n]: ";
        cin >> c;
        if(c == 'y' || c == 'Y'){
            break;
        }else{
            continue;
        }
    }
    return product;
}


Employee getEmployeeInfo(){
    Employee employee;
    char c = 'n';
    cout << "Add New Employee." <<endl;
    while(1){
        cout << "Enter The following information: " <<endl;
        cout << "Employee Id: " ;
        if (!(cin >> employee.Id)) {
            cout <<"Id should be a number\n\n"<<endl;
            cin.clear();
            cin.ignore(10000,'\n');
            continue;
        }

        cin.ignore();
        cout << "Employee Name: ";
        getline(cin, employee.Name);
        cout << "Employee Age: " ;
        if (!(cin >> employee.Age)) {
            cout <<"Age should be a number\n\n"<<endl;
            cin.clear();
            cin.ignore(10000,'\n');
            continue;
        }
        cout << "Employee Mobile: " ;
        if (!(cin >> employee.Mobile)) {
            cout <<"Mobile should be a number\n\n"<<endl;
            cin.clear();
            cin.ignore(10000,'\n');
            continue;
        }
        cin.ignore();
        cout << "Employee Address: " ;
        getline(cin, employee.Address);

        cout << "Id: " << employee.Id << ", Name: " << employee.Name << ", Age: "  <<  employee.Age << ", Mobile: " << employee.Mobile << ", Address: " << employee.Address <<endl;
        cout << "correct information ? [y/n]: ";
        cin >> c;
        if(c == 'y' || c == 'Y'){
            break;
        }else{
            continue;
        }
    }
    return employee;

}

void saveEmployee(Employee *employee)
{
        fstream employeeData;
        char* file = "employeeData.csv";

        employeeData.open(file, ios_base::out | ios_base::in);  // will not create file

        if (!employeeData.is_open()){
            employeeData.clear();
            employeeData.open (file,ios_base::app);
            employeeData  << "ID,Name,Age,Mobile,Address" << endl;
        }else{
            employeeData.close();
            employeeData.open (file,ios_base::app);
        }
        employeeData << employee->Id << ",\"" << employee->Name << "\"," << employee->Age << "," << employee->Mobile << ",\"" << employee->Address << "\""<< endl;
        cout << "Successfully added a new employee."<< endl;

        employeeData.close();
}

int listProducts(){

        string  text,i;
        char* file = "productsData.csv";
        ifstream productsData(file);

        if (!productsData.is_open()){
            cout<<"No Products"<<endl;
            return 0;
        }

        cout << "Products List:\n"<<endl;
        for (string text; getline(productsData, text); )
        {
            istringstream line;
            line.str(text);
            for (string i; getline(line, i,',');){
                cout << i << "\t";
            }
            cout << endl;
        }
            productsData.close();
        return 1;
}
int listEmployees(){

        string  text,i;
        char* file = "employeeData.csv";
        ifstream employeeData(file);

        if (!employeeData.is_open()){
            cout<<"No Employees"<<endl;
            return 0;
        }

        cout << "Employees List:\n"<<endl;
        for (string text; getline(employeeData, text); )
        {
            istringstream line;
            line.str(text);
            for (string i; getline(line, i,',');){
                cout << i << "\t";
            }
            cout << endl;
        }
            employeeData.close();
        return 1;
}

int listPurchases(){

        string  text,i;
        char* file = "productPurchases.csv";
        ifstream PurchasesData(file);

        if (!PurchasesData.is_open()){
            cout<<"No Purchases"<<endl;
            return 0;
        }

        cout << "Purchases List:\n"<<endl;
        for (string text; getline(PurchasesData, text); )
        {
            istringstream line;
            line.str(text);
            for (string i; getline(line, i,',');){
                cout << i << "\t";
            }
            cout << endl;
        }
            PurchasesData.close();
        return 1;
}

void saveProduct(Product *product)
{
        fstream productData;
        char* file = "productsData.csv";

        productData.open(file, ios_base::out | ios_base::in);  // will not create file
        if (!productData.is_open()){
            productData.clear ();
            productData.open (file,ios_base::app);
            productData  << "ID,Name,Description" << endl;
        }else{
            productData.close();
            productData.open (file,ios_base::app);
        }


        productData << product->Id << ",\"" << product->Name << "\",\"" << product->Description << "\""<< endl;
        cout << "Successfully added a new product."<< endl;
        productData.close();
}

void buyProduct(){
    char c = 'n';
    int product_id,employee_id,chk;
    chk = listProducts();
    if(!chk){
        cout<<"Add a product first before purchasing"<<endl;
        return;
    }
    cout << "Choose product:" <<endl;
    while(1){
        cout << "Product Id: " ;
        if (!(cin >> product_id)) {
            cout <<"product id should be a number\n\n"<<endl;
            cin.clear();
            cin.ignore(10000,'\n');
            continue;
        }
        break;
}

    chk = listEmployees();
    if(!chk){
        cout<<"Add an employee first before purchasing"<<endl;
        return;
    }
    cout << "Choose employee:" <<endl;
    while(1){
        cout << "Employee Id: " ;
        if (!(cin >> employee_id)) {
            cout <<"employee id should be a number\n\n"<<endl;
            cin.clear();
            cin.ignore(10000,'\n');
            continue;
        }
        break;

    }

        fstream productPurchases;
        char* file = "productPurchases.csv";

        productPurchases.open(file, ios_base::out | ios_base::in);  // will not create file
        if (!productPurchases.is_open()){
            productPurchases.clear ();
            productPurchases.open (file,ios_base::app);
            productPurchases  << "ProductID,EmployeeID" << endl;
        }else{
            productPurchases.close();
            productPurchases.open (file,ios_base::app);
        }


        productPurchases << product_id << "," << employee_id << endl;
        cout << "Successfully logged new product purchase."<< endl;
        productPurchases.close();

}
int main(void)
{
    int c;
    cout << "Employees Purchase management System" <<endl;

    while(1){
        cout << "Please choose an option: "<<endl;
        cout <<"l. List Employees."<<endl;
        cout <<"2. List Products."<<endl;
        cout <<"3. List Purchases."<<endl;
        cout <<"4. Add Employee"<<endl;
        cout <<"5. Add Product"<<endl;
        cout <<"6. Purchase a Product"<<endl;
        cout <<"7. Exit the Application"<<endl;
        cout << "your choice [1/2/3/4/5/6/7]: ";
        cin >> c;
        switch(c){
           case 1:
              listEmployees();
              break; //optional
           case 2:
              listProducts();
              break; //optional
           case 3:
              listPurchases();
              break; //optional
           case 4:
				{Employee employee = getEmployeeInfo();
				saveEmployee(&employee);}
              break; //optional
           case 5:
				{Product product = getProductInfo();
				saveProduct(&product);}
              break; //optional
           case 6:
                buyProduct();
                break;
           case 7:
                return 0;
                break;
           default : //Optional
              {
                  cout<<"Not a valid choice.\n\n"<<endl;
                  cin.clear();
                  cin.ignore(10000,'\n');
              }

        }

    }
	return 0;
}

