// main.dart
// import 'package:firebase_connection/home_page.dart';
import 'package:firebase_connection/home_page.dart';
//import 'package:firebase_connection/login.dart';
import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';

//import 'login.dart'; // Importez le fichier login.dart

void main() async {
  WidgetsFlutterBinding
      .ensureInitialized(); // Assure-toi que Flutter est initialisé
  await Firebase.initializeApp(); // Initialise Firebase
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mon Application',
      theme: ThemeData(primarySwatch: Colors.blue),
      home:
          const NavigationExample(), // Définissez LoginScreen comme écran principal
    );
  }
}
