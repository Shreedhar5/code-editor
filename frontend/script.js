let editor;
const term = new Terminal({ cursorBlink: true });
term.open(document.getElementById('terminal'));

// Load Monaco
require.config({ paths: { 'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.34.0/min/vs' } });
require(['vs/editor/editor.main'], () => {
  editor = monaco.editor.create(document.getElementById('editor'), {
    value: 'print("Hello, world!")',
    language: 'python',
    theme: 'vs-dark',
    automaticLayout: true
  });
});

document.getElementById('runBtn').addEventListener('click', async () => {
  term.clear();
  const code = editor.getValue();
  const input = document.getElementById('input').value;

  try {
    const res = await fetch('http://localhost:5000/run', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code, input })
    });
    const data = await res.json();
    term.writeln(data.output);
  } catch (err) {
    term.writeln('Error: ' + err.message);
  }
});
