 import { Component } from '@angular/core';
import {RouterModule} from '@angular/router';
@Component({
  selector: 'app-login-screen',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './login-screen.component.html',
  styleUrl: './login-screen.component.css'
})
export class LoginScreenComponent {


  onSubmit() {
    // 1. Récupérer les valeurs du formulaire (email et mot de passe)
    // 2. Envoyer une requête au backend Flask pour authentifier l'utilisateur
    // 3. En cas de succès, rediriger l'utilisateur vers la page d'accueil
    // 4. En cas d'erreur, afficher un message d'erreur


  }
}
