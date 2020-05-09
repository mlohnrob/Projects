import 'package:qsik/services/navigation_service.dart';
import 'package:qsik/locator.dart';
import 'package:stacked/stacked.dart';

class StartUpViewModel extends BaseViewModel {
  final NavigationService _navigationService = locator<NavigationService>();
  Future handleStartUpLogic() async {}
}
