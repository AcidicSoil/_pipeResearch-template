# DevOps

## Hosting
- **Frontend (Flutter Web):** Vercel (for static SPA builds)
- **Backend:** Supabase Edge Functions (hosted with Supabase project)
- **Database:** Supabase Postgres (with automatic scaling and backups)

## CI/CD
- **GitHub Actions**
  - Lint & format check (Flutter + Dart)
  - Automated testing (unit + integration)
  - Build artifacts for web and mobile
  - Deploy frontend to Vercel
  - Push edge functions to Supabase

```yaml
name: CI Pipeline
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.19.0'
      - run: flutter pub get
      - run: flutter analyze
      - run: flutter test
```

## Monitoring
- **Frontend & Mobile:** Sentry SDK for Dart/Flutter
- **Backend Functions:** Supabase Logs + Sentry integration
- **Performance Dashboards:** Vercel Analytics + Supabase Logs

## Backups
- Supabase daily snapshots (automatic)
- Manual backups via Supabase UI
- Retention: 7-day (free), 30-day (Pro)

## Scaling
- **Flutter Web:** Vercel edge CDN + static caching
- **Mobile:** Native runtime, no scaling needed
- **Backend:** Supabase Edge Functions auto-scale with usage
- **Database:** PostgreSQL auto-scaling + read replica (Pro tier)

## Environment Management

### Development
- Local Flutter development with hot reload
- Local Supabase instance via Docker
- Development database with sample data
- Environment variables via `.env.development`

### Staging
- Dedicated Supabase project for staging
- Test user accounts
- Mirrors production configuration
- Environment variables via `.env.staging`

### Production
- Live Supabase project with rate limiting
- Production database with backups
- CI/CD enforced deployment checks
- Environment variables via `.env.production`

## Security Practices
- JWT token rotation
- API rate limiting
- Database connection encryption
- Regular security audits
- Automated vulnerability scanning
- No secrets in code repositories