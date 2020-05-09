import 'package:qsik_spotify/services/navigation_service.dart';
import 'package:qsik_spotify/locator.dart';
import 'package:stacked/stacked.dart';

class StartUpViewModel extends BaseViewModel {
  final NavigationService _navigationService = locator<NavigationService>();
  Future handleStartUpLogic() async {}
}
