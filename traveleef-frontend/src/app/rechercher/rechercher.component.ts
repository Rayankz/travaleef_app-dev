import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'; // Import du CommonModule


@Component({
  selector: 'app-rechercher',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './rechercher.component.html',
  styleUrls: ['./rechercher.component.css']
})
export class RechercherComponent {
  // Données pour les résultats de recherche
  results = [
    {
      trajet: 'Paris -> Manchester',
      duree: '4h',
      co2: '106kg CO2/Pers.',
      transportIcons: ['✈️', '🚆'],
      price: '40€/pers.',
      details: [
        {
          from: 'Paris (cdg)',
          to: 'Londres (lhr)',
          time: '10H30',
          co2: '80kg',
          company: 'Air France'
        },
        {
          from: 'Londres (lhr)',
          to: 'Manchester Piccadilly',
          time: '12H30',
          co2: '26kg'
        }
      ]
    },
    {
      trajet: 'Paris -> New York',
      duree: '8H20',
      co2: '1450kg CO2/Pers.',
      transportIcons: ['✈️'],
      price: '450€/pers.',
      details: [
        {
          from: 'Paris (cdg)',
          to: 'New York (jfk)',
          time: '10H30',
          co2: '1450kg',
          company: 'Air France'
        }
      ]
    }
  ];
}
