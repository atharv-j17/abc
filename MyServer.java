package demo;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class MyServer {
    public static void main(String[] args) {
        try {
            MyInterface obj = new MyRemoteClass();
            LocateRegistry.createRegistry(1099); 
            Naming.rebind("MyRemoteClass", obj); 
            System.out.println("MyRemoteClass bound in registry");
        } catch (Exception e) {
            System.err.println("MyRemoteClass exception:");
            e.printStackTrace();
        }
    }
}
