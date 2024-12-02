import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-historique',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './historique.component.html',
  styleUrls: ['./historique.component.css']
})
export class HistoriqueComponent {
  voyages = [
    {
      trajet: 'Paris -> New York',
      duree: '8H20',
      prix: '500€',
      dates: 'du 10/10/2099 au 10/11/2099',
    },
    {
      trajet: 'Paris -> Marseille',
      duree: '4h',
      prix: '50€',
      dates: 'du 10/12/2099 au 10/12/2099',
    },
    {
      trajet: 'Paris -> New York',
      duree: '8H20',
      prix: '500€',
      dates: 'du 10/10/2099 au 10/11/2099',
    },
  ];
}
