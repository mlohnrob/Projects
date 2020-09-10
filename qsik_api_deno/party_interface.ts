export interface Party {
  readonly id: string;
  readonly owner: string;
  readonly name: string;
  readonly maxPeople: number;
  people: Array<String>;
}
