
export function randomItemFromList<Type>(arr: Type[]): Type | null {
    if (arr.length == 0) return null;
    return arr[Math.floor(Math.random() * arr.length)];
}
