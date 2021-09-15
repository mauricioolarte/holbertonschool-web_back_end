export default function guardrail(mathFunction) {
  const queue = [];
  let valor;

  try {
    valor = mathFunction();
  } catch (err) {
    valor = err.toString();
  }

  queue.push(valor);
  queue.push('Guardrail was processed');

  return queue;
}
