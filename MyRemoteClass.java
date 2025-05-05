package demo;

import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;

public class MyRemoteClass extends UnicastRemoteObject implements MyInterface {
    public MyRemoteClass() throws RemoteException {
        super();
    }

    public String sayHello() throws RemoteException {
        return "Hello, world!";
    }
}
