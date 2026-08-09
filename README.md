# Quanto stimola ogni esercizio

Riferimento clinico di elettromiografia per la riabilitazione: attivazione muscolare per esercizio, espressa in percentuale della massima contrazione volontaria isometrica (%MVIC), aggregata da diciassette studi peer-reviewed.

Pagina singola, nessuna dipendenza, nessun build. Apri `index.html` in un browser.

## Cosa contiene

**Esercizi** — grafici a barre orizzontali per muscolo, con ricerca e filtri. Cinque distretti:

| Distretto | Schede |
|---|---|
| Spalla | sovraspinato, infraspinato, sottoscapolare, piccolo rotondo, deltoidi (ant./med./post.), trapezio (sup./medio/inf.), dentato anteriore |
| Anca | gluteo medio, grande gluteo, TFL |
| Coscia | vasto mediale, vasto laterale, retto femorale (prossimale/mediale), quadricipite globale |
| Ischiocrurali | semitendinoso, bicipite femorale, semimembranoso |
| Polpaccio | tricipite surale, gastrocnemio mediale |

**Continuum** — progressioni cliniche divise per distretto: spalla, quadricipite, ischiocrurali, polpaccio.

**Metodo** — come ogni studio ha normalizzato, e perché alcuni studi non compaiono nei grafici.

## Le soglie

La linea tratteggiata cambia significato con l'obiettivo, e compare solo dove ha senso:

- **15% MVIC** — tetto di carico dopo riparazione di cuffia dei rotatori (schede cuffia e deltoide)
- **40% MVIC** — soglia di rinforzo per il quadricipite
- **70% MVIC** — soglia di rinforzo usata negli studi sui glutei
- **nessuna soglia** — schede scapolari, TFL, ischiocrurali, polpaccio

Sulle schede scapolari la soglia manca di proposito: quello studio cercava la massima attivazione per il rinforzo, non il carico minimo per proteggere una riparazione, e va letto dall'alto verso il basso.

## Attenzione ai denominatori

**Non tutte le schede stanno sulla stessa scala.** Tre metodi di normalizzazione convivono nell'app:

- **%MVIC** — massima contrazione volontaria isometrica. La maggior parte delle schede
- **% del picco durante sprint** — ischiocrurali e gastrocnemio mediale
- **EMG medio sulla serie invece del picco** — quadricipite globale

La scala di ogni riga è indicata sotto il nome dell'esercizio. Confronta i numeri dentro la stessa scheda, non fra schede diverse, e mai fra denominatori diversi.

Due schede riportano valori letti dalle figure degli articoli anziché da tabelle (ischiocrurali) o ricavati per differenza (gastrocnemio mediale a escursione neutra). Le righe interessate lo dichiarano.

## Studi inclusi

Spalla — Edwards 2017, Edwards 2021, Ekstrom 2003, Kang 2019, Januario 2022
Anca — Selkowitz 2013, Boren 2011, Goller 2024
Coscia — Vera-Cartagena 2026, Marshall 2020, Karst 1993
Ischiocrurali — van den Tillaar 2017, Ferri-Caruana 2022
Polpaccio — Mullaney 2011, Ferri-Caruana 2025, Cibulka 2017, Nunes 2020, Ugbolue 2021

Riferimenti completi in fondo alla pagina. Cinque studi non compaiono nei grafici perché non normalizzano su una MVIC o perché i valori esistono solo dentro le figure: il loro contenuto è nel Continuum e nel Metodo.

## File

Tutti nella radice del repository:

| File | A cosa serve |
|---|---|
| `index.html` | l'app: struttura, stili, dati e logica in un unico file |
| `manifest.json` | permette l'installazione sulla schermata home |
| `sw.js` | service worker: fa funzionare l'app senza connessione |
| `icon-*.png`, `apple-touch-icon.png`, `favicon.png` | icone |
| `README.md` | questa scheda, facoltativa |

## Aggiornare l'app

Sostituisci `index.html` **e** incrementa `CACHE` in `sw.js` (`emg-v1` → `emg-v2`). Senza il secondo passaggio i telefoni che hanno già installato l'app continueranno a servire la versione vecchia dalla cache.

## Cambiare i colori dell'icona

Le icone sono generate da `make_icons.py`: modifica le due costanti `BG` e `BOLT` in cima al file e rilancialo.

## Pubblicare su GitHub Pages

1. Carica tutti i file nella radice del repository
2. Settings → Pages → Source: `Deploy from a branch`, branch `main`, cartella `/ (root)`
3. La pagina sarà su `https://<utente>.github.io/<repo>/`

I font arrivano da Google Fonts via CDN: serve connessione. Per un uso completamente offline, rimuovi i tre tag `<link>` nell'`<head>` — il layout regge sui font di sistema.

## Limiti

L'EMG stima il carico, non lo misura, e l'ampiezza del segnale non predice l'adattamento a lungo termine. Le soglie qui riportate sono una guida alla scelta e alla progressione degli esercizi, non una garanzia di sicurezza per un tessuto riparato. Nessuna di queste schede sostituisce il giudizio clinico sul singolo paziente.

I dati provengono da studi su soggetti in larga maggioranza sani, spesso giovani e di un solo sesso. I limiti di ciascuno studio sono riportati nelle card del Metodo.

## Licenza

Il codice è liberamente riutilizzabile. I dati sono estratti da pubblicazioni scientifiche: quelle open access sono indicate come CC BY 4.0 in bibliografia, le altre restano soggette al copyright dei rispettivi editori e sono qui riportate come valori numerici con attribuzione.
