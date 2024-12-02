import { CommonModule, isPlatformBrowser } from '@angular/common';
import { Component, AfterViewInit, Inject, PLATFORM_ID } from '@angular/core';

@Component({
  selector: 'app-accueil',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './accueil.component.html',
  styleUrls: ['./accueil.component.css']
})
export class AccueilComponent implements AfterViewInit {
  private map: any; // Utilisation de `any` pour éviter les problèmes côté serveur

  // Données pour les suggestions de voyages
  suggestions = [
    {
      trajet: 'Montreuil - Marseille',
      depart: 'Montreuil, France',
      arrivee: 'Marseille, France',
      emissions: '12 kg de CO2/km',
      duree: '5h',
      modes: 'TGV - Bus',
      prix: '40€'
    },
    {
      trajet: 'Montreuil - Lyon',
      depart: 'Montreuil, France',
      arrivee: 'Lyon, France',
      emissions: '10 kg de CO2/km',
      duree: '4h',
      modes: 'Train',
      prix: '35€'
    },
    {
      trajet: 'Montreuil - Bordeaux',
      depart: 'Montreuil, France',
      arrivee: 'Bordeaux, France',
      emissions: '15 kg de CO2/km',
      duree: '6h',
      modes: 'TGV - Bus',
      prix: '50€'
    },
  ];

  constructor(@Inject(PLATFORM_ID) private platformId: Object) {}

  async ngAfterViewInit(): Promise<void> {
    // Vérifie si le code s'exécute dans le navigateur avant d'initialiser Leaflet
    if (isPlatformBrowser(this.platformId)) {
      const L = await import('leaflet'); // Import dynamique de Leaflet uniquement côté client

      this.initMap(L); // Passe Leaflet comme argument pour éviter les erreurs
    }
  }

  // Initialisation de la carte
  private initMap(L: any): void {
    this.map = L.map('map', {
      center: [48.8566, 2.3522], // Coordonnées de Paris
      zoom: 13 // Niveau de zoom initial
    });

    // Ajout du fond de carte OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
    }).addTo(this.map);
  }
}
