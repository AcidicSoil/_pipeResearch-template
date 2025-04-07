# Third-Party Libraries

## Frontend (Flutter)
- `flutter_riverpod` – State management
- `drift` – Offline local database (SQLite abstraction)
- `http` – REST API client
- `flutter_secure_storage` – Secure token storage
- `shared_preferences` – Local settings
- `flutter_markdown` – Rich AI assistant UI rendering
- `sentry_flutter` – Error monitoring
- `uuid` – Unique ID generation
- `flutter_dotenv` – Environment variables

## Backend (Supabase + Edge Functions)
- **Supabase** – Postgres + Auth + Storage + Edge Functions
- **OpenAI API** – LLM functions for Assistant (text-to-action, summarization)
- **Swagger/OpenAPI** – API schema generation and documentation

## CI/CD & Monitoring
- **GitHub Actions** – Automated tests, builds, deploys
- **Sentry.io** – Full-stack error tracking (Flutter + Supabase)
- **Vercel Analytics** – Performance dashboards for Flutter Web

## Testing
- `flutter_test` – Unit testing
- `integration_test` – Integration testing
- `mockito` – Mocking dependencies

## Documentation & Visualization
- `mermaid.js` – Architecture & user flow diagrams
- `supabase-openapi` – Swagger docs for Supabase edge functions

## Licensing
- All packages used are MIT/BSD/Apache licensed (per Flutter and Supabase ecosystem)
- OpenAI used under commercial license via API key

## Dependencies Management

### Frontend Dependencies

```yaml
# pubspec.yaml
dependencies:
  flutter:
    sdk: flutter

  # State Management
  flutter_riverpod: ^2.3.6

  # Database & Storage
  drift: ^2.8.0
  sqlite3_flutter_libs: ^0.5.15
  path_provider: ^2.0.15
  path: ^1.8.3
  flutter_secure_storage: ^8.0.0
  shared_preferences: ^2.1.1

  # Networking
  http: ^0.13.6
  connectivity_plus: ^4.0.1
  supabase_flutter: ^1.10.3

  # UI Components
  flutter_markdown: ^0.6.15
  intl: ^0.18.0
  url_launcher: ^6.1.11

  # Utils
  uuid: ^3.0.7
  flutter_dotenv: ^5.0.2

  # Monitoring
  sentry_flutter: ^7.5.2

dev_dependencies:
  flutter_test:
    sdk: flutter
  integration_test:
    sdk: flutter
  mockito: ^5.4.0
  drift_dev: ^2.8.0
  build_runner: ^2.4.5
  flutter_lints: ^2.0.1
```

### Backend Dependencies

```json
// package.json (Supabase Edge Functions)
{
  "name": "ai-secretary-functions",
  "version": "1.0.0",
  "description": "Edge functions for AI Secretary app",
  "dependencies": {
    "@supabase/supabase-js": "^2.21.0",
    "openai": "^3.2.1",
    "date-fns": "^2.30.0",
    "zod": "^3.21.4"
  },
  "devDependencies": {
    "typescript": "^5.0.4",
    "supabase": "^1.55.1"
  }
}
```

## Version Compatibility

| Package | Version | Compatibility Notes |
|---------|---------|---------------------|
| flutter | 3.10.0+ | Required for latest features |
| dart | 3.0.0+ | Required for pattern matching |
| flutter_riverpod | ^2.3.6 | Not compatible with v1.x |
| drift | ^2.8.0 | Requires SQLite 3.35.0+ |
| supabase_flutter | ^1.10.3 | Compatible with Supabase v2 API |
| openai | ^3.2.1 | Compatible with ChatGPT and DALL-E APIs |

## Update Process
- Dependencies updated monthly
- Major version bumps require thorough testing
- Security vulnerabilities addressed immediately
- Changelog maintained at `CHANGELOG.md`