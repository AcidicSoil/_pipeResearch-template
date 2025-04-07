# Testing Plan

## Unit Tests
- **Scope:** Pure Dart logic, Riverpod providers, utility functions
- **Framework:** `flutter_test`, `mockito`
- **Examples:**
  - Task and event model validation
  - LLM function call handler logic
  - Sync conflict resolution strategies

## Integration Tests
- **Scope:** Widget + API + local DB interaction
- **Tools:** `integration_test`, `drift_test`
- **Examples:**
  - Add/edit/delete task with local DB + Supabase sync
  - Offline task creation → sync on reconnect

## End-to-End (E2E)
- **Scope:** Real device/browser flows
- **Tools:** `Flutter Driver`, `E2E plugin`, `Firebase Test Lab`
- **Examples:**
  - Full onboarding to dashboard flow
  - AI chat → task creation → confirmation display

## Exploratory Testing
- **Scope:** Manual QA across devices
- **Tools:** TestRail, Notion checklists, BrowserStack for cross-device
- **Focus:**
  - Error boundary triggers
  - Offline/online edge cases
  - Cross-platform visual inconsistencies

## CI Testing
- All unit + integration tests run on GitHub Actions for every PR
- E2E scheduled nightly on staging

## Test Coverage Requirements

### Critical Paths (100% Coverage)
- Authentication flows
- Task CRUD operations
- Calendar CRUD operations
- Offline sync logic

### High Priority (80%+ Coverage)
- LLM function call handlers
- UI navigation flows
- Form validations
- Error handling

### Medium Priority (60%+ Coverage)
- UI component rendering
- Theming and styles
- Performance optimizations

## Test Data Management
- Fixture generation for consistent test data
- Database seeding scripts for integration tests
- Mock API responses for offline testing

## Test Environments
- **Local:** Developer machine with emulator/simulator
- **CI:** GitHub Actions with emulator matrix
- **Device Lab:** Firebase Test Lab with real device matrix
- **Staging:** Mirror of production with test data

## Testing Schedule
- **Pre-commit:** Lint + unit tests
- **PR:** Unit + integration tests
- **Nightly:** Full suite including E2E
- **Pre-release:** Manual QA + full automated suite

## Reporting
- GitHub Actions test summaries
- Code coverage reports via Codecov
- TestRail for manual test case tracking
- Bug tracking via GitHub Issues