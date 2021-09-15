export default function guardrail(mathFunction) {
  const list = [];
  let valores;

  try {
    valores = mathFunction();
  } catch (err) {
    valores = err.toString();
  }

  list.push(value);
  list.push('Guardrail was processed');

  return list;
}

