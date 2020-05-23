export default function getRequestOpts(method: string): RequestInit {
  return {
    credentials: 'same-origin',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    method: method,
  };
}
