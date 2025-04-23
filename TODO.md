# 🛠️ Django No-Code Admin-Modul – Projektübersicht

Ein visuelles Django-Admin-Modul zur vollständigen Konfiguration von Models, Feldern, Benutzerrechten, Datenbankrouting und UI – komplett ohne Code.

---

## ✅ TODO-Liste

### 1. Grundstruktur
- [ ] Neues Django-App-Modul erstellen
- [ ] Admin-Panel erweitern oder separates Dashboard bauen
- [ ] Zugriff nur für Superuser oder bestimmte Gruppen

---

### 2. Model-Verwaltung (Model Builder)
- [ ] Models via GUI erstellen (Name, Meta-Optionen)
- [ ] Felder hinzufügen (Typ, Optionen, Validierung, Defaults, Beziehungen)
- [ ] Bestehende Models ändern (inkl. Versionierung)
- [ ] Automatische Migrations-Erstellung und Anwendung

---

### 3. Multi-Database Support
- [ ] Unterstützung für mehrere Datenbanken (MySQL, PostgreSQL, SQLite, etc.)
- [ ] Datenbank pro Model auswählbar
- [ ] Dynamischer Database-Router auf Basis von Model-Zuweisung

---

### 4. Admin-Darstellung (UI Configurator)
- [ ] Spaltenanzeige, Filter, Suchfelder anpassbar
- [ ] Inline-Formulare & Autocomplete aktivierbar
- [ ] Darstellung abhängig von Userrollen
- [ ] Custom Hooks: Formatierungen vor/nach Speichern

---

### 5. Form Builder
- [ ] Formulare via GUI erstellen
- [ ] Widgets & Validierungsregeln auswählbar
- [ ] Abhängigkeiten zwischen Feldern definierbar

---

### 6. Benutzer- & Gruppenrechte
- [ ] CRUD-Rechte pro Model/Feld festlegen
- [ ] Rollen und Zugriffsebenen definieren
- [ ] Dynamische Sichtbarkeit (z. B. Feld nur sichtbar bei bestimmtem Wert)

---

### 7. Export / Import / Backup
- [ ] Model- und Admin-Configs als JSON/YAML exportieren
- [ ] Importfunktion für andere Projekte
- [ ] Backup vor Migrationen

---

## 💡 Erweiterungsideen

- [ ] **Live-Vorschau** von Admin-Änderungen
- [ ] **Audit Logging**: Wer hat wann was geändert?
- [ ] **Reverse Engineering**: Bestehende DB → Model-Struktur
- [ ] **REST API Builder**: Automatisch DRF-Endpoints für Models
- [ ] **Theme-Management** für Admin (Dark Mode, Custom Styles)
- [ ] **Mehrsprachigkeit** für Feldnamen und Admin-Texte
- [ ] **AI-gestützte Felderkennung** (z. B. bei Namen wie "price" → DecimalField)
- [ ] **Signals per UI**: Trigger wie "Nach dem Speichern E-Mail versenden"

---

## 📁 Optional: Tech Stack & Architektur

- **Frontend**: Django Admin, oder eigenes Interface (React/Vue)
- **Backend**: Django REST Framework (für dynamische Konfigurationen)
- **Datenhaltung**: Konfigurationen in eigener Modelstruktur (JSONField oder YAML)
- **Security**: Granulare Rechtevergabe, Logging, Validierung

---

## ✨ Ziel

Ein zentrales Tool für Entwickler:innen, Admins und Projektleiter:innen zur vollständigen Verwaltung eines Django-Projekts ohne direkte Codeänderung.

