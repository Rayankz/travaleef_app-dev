import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule, HttpParams } from '@angular/common/http';

@Component({
  selector: 'app-rechercher',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule], // Ajout de HttpClientModule ici
  templateUrl: './rechercher.component.html',
  styleUrls: ['./rechercher.component.css']
})
export class RechercherComponent {
  departureId: string = '';
  arrivalId: string = '';
  outboundDate: string = '';
  returnDate: string = '';
  passengerCount: number = 1;

  results: any[] = [];
  errorMessage: string = '';

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
        this.errorMessage = '';
      },
      error: (error) => {
        this.errorMessage = `Erreur : ${error.message}`;
        this.results = [];
      }
    });
  }
}
