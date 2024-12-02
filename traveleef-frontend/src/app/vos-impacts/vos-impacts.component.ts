import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'; // Import du CommonModule

@Component({
  selector: 'app-vos-impacts',
  standalone: true,
  imports: [CommonModule], // Ajoutez CommonModule ici
  templateUrl: './vos-impacts.component.html',
  styleUrls: ['./vos-impacts.component.css']
})
export class VosImpactsComponent {
  // Exemple de données pour les impacts environnementaux
  impacts = [
    { type: 'Avion', emission: 23 },
    { type: 'Voiture', emission: 18 },
    { type: 'Train', emission: 12 }
  ];
}
