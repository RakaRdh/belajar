/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package projectoop;

import java.util.*;
import java.io.*;

public class MainProgram {
    public static void main(String[] args) {
        // Membuat objek ManajemenKaryawan
        AccountManagement manage = new AccountManagement();
        Scanner scanner = new Scanner(System.in);

        try {
            String namaFile = "akun.txt";
            File file = new File(namaFile);
            if (!file.exists()) {
                System.out.println("File " + namaFile + " tidak ditemukan.");
                System.out.println("Membuat file baru...");
                file.createNewFile();
            } else {
                BufferedReader reader;
                reader = new BufferedReader(new FileReader(namaFile));
                String line;
                while ((line = reader.readLine()) != null) {
                    String[] accountData = line.split(";");
                    String username = accountData[0];
                    String type = accountData[1];
                    String email = accountData[2];
                    String phoneNumber = accountData[3];
                    String nik = accountData[4];
                    double balance = Double.parseDouble(accountData[5]);
                    String password = accountData[6];

                    // Perbarui data akun di accountList
                    manage.updateAccount(username, type, email, phoneNumber, nik, balance, password);
                }
                reader.close();
            }
        } catch (IOException e) {
            System.err.println("Gagal membaca file.");
        }

        // Menu login
        boolean exit = false;
        while (!exit) {
            System.out.println("===========================================");
            System.out.println("1. Login");
            System.out.println("2. Register");
            System.out.println("3. Exit");
            System.out.println("==========================================");
            System.out.print("Select menu: ");

            String pilihan = scanner.next();
            scanner.nextLine(); // Membersihkan buffer

            switch (pilihan) {
                case "1":
                    loginAccount(scanner, manage);
                    break;
                case "2":
                    registerAccount(scanner, manage);
                    manage.saveAccount("akun.txt");
                    break;
                case "3":
                    exit = true;
                    break;
                default:
                    System.out.println("Invalid Menu.");
            }
        }
        
    }

    public static void menu(Scanner scanner, AccountManagement manage, Account loggedInAccount) {
        // Menampilkan menu
        boolean exit = false;
        while (!exit) {
            System.out.println("================= Welcome =================");
            System.out.println("1. View Account");
            System.out.println("2. Add Balance");
            System.out.println("3. Transfer");
            System.out.println("4. Withdraw Balance");
            System.out.println("5. Upgrade to Premium");
            System.out.println("6. Logout");
            System.out.println("==========================================");
            System.out.print("Select menu: ");
            String pilihan = scanner.next();
            scanner.nextLine(); // Membersihkan buffer

            switch (pilihan) {
                case "1":
                    manage.viewAccount(loggedInAccount);
                    break;
                case "2":
                    manage.addBalance(scanner, loggedInAccount);
                    break;
                case "3":
                    manage.transferBalance(scanner, loggedInAccount);
                    break;
                case "4":
                    manage.withdrawBalance(scanner, loggedInAccount);
                    break;
                case "5":
                    manage.statusUpgrade(scanner, loggedInAccount);
                    break;
                case "6":
                    exit = true;
                    break;
                default:
                    System.out.println("Invalid menu.");
            }
        }

        
    }

    public static void loginAccount(Scanner scanner, AccountManagement accountManagement) {
        System.out.print("Enter Username: ");
        String username = scanner.nextLine();
        System.out.print("Enter Password: ");
        String password = scanner.nextLine();

        Account loggedInAccount = accountManagement.loginAccount(username, password);

        if (loggedInAccount != null) {
            System.out.println("Login successful!");
            menu(scanner, accountManagement, loggedInAccount);
        } else {
            System.out.println("Invalid username or password.");
        }
    }

    public static void registerAccount(Scanner scanner, AccountManagement manage) {
        System.out.print("Enter Username: ");
        String username = scanner.nextLine();
        System.out.print("Enter Email: ");
        String email = scanner.nextLine();

        String password;
        String confirmPassword;
        do {
            System.out.print("Enter Password: ");
            password = scanner.nextLine();
            System.out.print("Confirm Password: ");
            confirmPassword = scanner.nextLine();

            if (!password.equals(confirmPassword)) {
                System.out.println("Passwords do not match. Please try again.");
            }
        } while (!password.equals(confirmPassword));

        System.out.print("Enter Phone Number: ");
        String phoneNumber = scanner.nextLine();

        manage.registerAccount(username, email, phoneNumber, password);
        System.out.println("Account created successfully. Please login.");
    }
}