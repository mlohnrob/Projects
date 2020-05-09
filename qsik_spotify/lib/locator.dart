import 'package:get_it/get_it.dart';
import 'package:qsik_spotify/services/dialog_service.dart';
import 'package:qsik_spotify/services/navigation_service.dart';

GetIt locator = GetIt.instance;

void setupLocator() {
  locator.registerLazySingleton(() => NavigationService());
  locator.registerLazySingleton(() => DialogService());
}
