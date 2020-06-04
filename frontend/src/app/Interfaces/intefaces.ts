export interface DataTable {
  id?: number;
  nombre: string;
  precio: number;
  codigoBarras: number;
  cantidad: number;
  fecha: string;
} 
export interface QueryData {
  data: DataTable[];
  totalResults: number;
} 