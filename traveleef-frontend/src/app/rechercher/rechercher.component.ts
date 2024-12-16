import { Component } from '@angular/core';
import { HttpClient, HttpParams, HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-rechercher',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './rechercher.component.html',
  styleUrls: ['./rechercher.component.css']
})
export class RechercherComponent {
  // Champs de recherche
  departureId: string = '';
  arrivalId: string = '';
  outboundDate: string = '';
  returnDate: string = '';
  passengerCount: number = 1;

  // Résultats des vols
  results: any[] = [];
  filteredResults: any[] = [];
  errorMessage: string = '';

  // Valeurs des filtres
  maxPrice: number = 10000;
  maxDuration: number = 5000; // en minutes
  maxCO2: number = 5000; // en kg

  // Popup pour les détails du vol
  selectedFlight: any = null;

  // URL de l'API backend
  private apiUrl = 'http://127.0.0.1:5000/api/recherche_vols';

  constructor(private http: HttpClient) {}

  rechercherVols(): void {
    if (!this.departureId || !this.arrivalId || !this.outboundDate) {
      this.errorMessage = 'Veuillez remplir tous les champs requis.';
      return;
    }

    let params = new HttpParams()
      .set('departure_id', this.departureId)
      .set('arrival_id', this.arrivalId)
      .set('outbound_date', this.outboundDate);

    if (this.returnDate) {
      params = params.set('return_date', this.returnDate);
    }

    this.http.get<any>(this.apiUrl, { params }).subscribe({
      next: (response) => {
        this.results = response.best_flights || [];
        this.filteredResults = [...this.results];
        this.errorMessage = '';
        this.applyFilters();
      },
      error: (error) => {
        this.errorMessage = `Erreur : ${error.message}`;
        this.results = [];
        this.filteredResults = [];
      }
    });
  }

  applyFilters(): void {
    this.filteredResults = this.results.filter((flight) => {
      const price = flight.price || 0;
      const duration = flight.total_duration || 0;
      const co2 = flight.carbon_emissions?.this_flight || 0;

      return price <= this.maxPrice && duration <= this.maxDuration && this.getCO2PerPerson(co2) <= this.maxCO2;
    });
  }

  // Calculer les émissions de CO₂ par personne
  getCO2PerPerson(totalCO2: number): number {
    return Math.round(totalCO2 / 250);
  }

  // Ouvrir les détails d'un vol
  openDetails(flight: any): void {
    this.selectedFlight = flight;
  }

  // Fermer les détails du vol
  closeDetails(): void {
    this.selectedFlight = null;
  }
}
