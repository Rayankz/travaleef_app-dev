import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VosImpactsComponent } from './vos-impacts.component';

describe('VosImpactsComponent', () => {
  let component: VosImpactsComponent;
  let fixture: ComponentFixture<VosImpactsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VosImpactsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(VosImpactsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
