import { NgModule } from '@angular/core';
import { Routes,RouterModule } from '@angular/router';
import { LoginScreenComponent } from './login-screen/login-screen.component';
import { SignupScreenComponent} from "./signup-screen/signup-screen.component";
import { VosImpactsComponent } from './vos-impacts/vos-impacts.component';
import { HistoriqueComponent } from './historique/historique.component';
import { AccueilComponent } from './accueil/accueil.component';
import { RechercherComponent } from './rechercher/rechercher.component';


export const routes: Routes = [
  //{ path: '', redirectTo: '/se-connecter', pathMatch: 'full' },
  { path: 'se-connecter', component: LoginScreenComponent },
  { path: 'vos-impacts', component: VosImpactsComponent },
  { path: 'historique', component: HistoriqueComponent },
  { path: 'creer-un-compte', component: SignupScreenComponent },
  { path: '', component: AccueilComponent },
  { path: 'rechercher', component: RechercherComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
