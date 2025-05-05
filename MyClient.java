package demo;

import java.rmi.Naming;

public class MyClient {
    public static void main(String[] args) {
        try {
            MyInterface obj = (MyInterface) Naming.lookup("//localhost/MyRemoteClass");
            System.out.println(obj.sayHello());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
