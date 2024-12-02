import { Component } from '@angular/core';
import { Router } from '@angular/router';
import {FormsModule} from "@angular/forms";

@Component({
  selector: 'app-signup-screen',
  templateUrl: './signup-screen.component.html',
  standalone: true,
  imports: [
    FormsModule
  ],
  styleUrls: ['./signup-screen.component.css']
})
export class SignupScreenComponent {

  constructor(private router: Router) { }

  onSubmit() {
    // 1. Récupérer les valeurs du formulaire
    // 2. Envoyer une requête au backend Flask pour créer le compte utilisateur
    // 3. En cas de succès, rediriger l'utilisateur vers la page de connexion ou d'accueil
    // 4. En cas d'erreur, afficher un message d'erreur

    // Exemple de redirection :
    this.router.navigate(['/se-connecter']);
  }
}
