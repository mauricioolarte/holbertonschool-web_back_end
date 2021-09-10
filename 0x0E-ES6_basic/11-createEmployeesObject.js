export default function createEmployeesObject(department, employees) {
  return {
    [department]: [...employees],
  };
}
